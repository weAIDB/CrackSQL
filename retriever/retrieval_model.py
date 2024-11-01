# -*- coding: utf-8 -*-
# @Project: xxxx
# @Module: retrieval_model
# @Author: xxxx
# @Time: 2024/9/1 19:13

import math
import json
import copy

import torch
import torch.nn as nn
import torch.nn.functional as F

from langchain_community.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer


# https://docs.llamaindex.ai/en/stable/examples/retrievers/bm25_retriever/
# https://stackoverflow.com/questions/77217193/langchain-how-to-use-a-custom-embedding-model-locally


class ContrastiveLossV1(nn.Module):
    def __init__(self, smooth=0):
        super().__init__()
        self.H = nn.CrossEntropyLoss(label_smoothing=smooth, reduction="mean")

    def forward(self, text_batch: torch.Tensor, code_batch: torch.Tensor, T=0.08):
        """
        :param text_batch: (N, D) logits batch with rows having norm=1
        :param code_batch: (N, D) logits batch with rows having norm=1
        :param T: Learnable temperature
        :return: scalar
        """

        text2code = text_batch @ code_batch.T
        code2text = code_batch @ text_batch.T

        gt_t = torch.arange(text_batch.shape[0], device=text_batch.device)
        gt_c = torch.arange(code_batch.shape[0], device=code_batch.device)
        loss = 0.5 * self.H(text2code / T, gt_t) + 0.5 * self.H(code2text / T, gt_c)

        return loss


class ContrastiveLossV2(nn.Module):
    def __init__(self, temperature=0.08):
        super(ContrastiveLossV2, self).__init__()
        self.temperature = temperature

    def forward(self, x, pos_indices):
        assert len(x.size()) == 2

        # Add indexes of the principal diagonal elements to pos_indices
        pos_indices = torch.cat([
            pos_indices,
            torch.arange(x.size(0)).reshape(x.size(0), 1).expand(-1, 2),
        ], dim=0).to(x.device)

        # Ground truth labels
        target = torch.zeros(x.size(0), x.size(0)).to(x.device)
        target[pos_indices[:, 0], pos_indices[:, 1]] = 1.0

        # Cosine similarity
        xcs = F.cosine_similarity(x[None, :, :], x[:, None, :], dim=-1)
        # Set logit of diagonal element to "inf" signifying complete
        # correlation. sigmoid(inf) = 1.0 so this will work out nicely
        # when computing the Binary Cross Entropy Loss.
        xcs[torch.eye(x.size(0)).bool()] = float("inf")

        # Standard binary cross entropy loss. We use binary_cross_entropy() here and not
        # binary_cross_entropy_with_logits() because of https://github.com/pytorch/pytorch/issues/102894
        # The method *_with_logits() uses the log-sum-exp-trick, which causes inf and -inf values
        # to result in a NaN result.
        loss = F.binary_cross_entropy((xcs / self.temperature).sigmoid(), target, reduction="none")

        target_pos = target.bool()
        target_neg = ~target_pos

        loss_pos = torch.zeros(x.size(0), x.size(0)).to(x.device).masked_scatter(target_pos, loss[target_pos])
        loss_neg = torch.zeros(x.size(0), x.size(0)).to(x.device).masked_scatter(target_neg, loss[target_neg])
        loss_pos = loss_pos.sum(dim=1)
        loss_neg = loss_neg.sum(dim=1)
        num_pos = target.sum(dim=1)
        num_neg = x.size(0) - num_pos

        return ((loss_pos / num_pos) + (loss_neg / num_neg)).mean()


class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads, dropout=0.1):
        super(MultiHeadAttention, self).__init__()
        assert d_model % num_heads == 0, "`d_model` can't be spiltted into `h` heads"
        # We assume d_v always equals d_k
        self.d_k = d_model // num_heads
        self.num_heads = num_heads
        self.linears = nn.ModuleList([nn.Linear(d_model, d_model) for _ in range(3 + 1)])
        # self.pool = nn.Linear(9, 1)
        self.attn_score = None
        self.dropout = nn.Dropout(p=dropout)

    def attention(self, query, key, value, mask=None, dropout=None):
        """
        Compute 'Scaled Dot Product Attention'
        :return:
        """
        # d_k = query.size(-1)
        scores = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(self.d_k)  # torch.Size([2, 4, 1, 1])
        if mask is not None:
            # scores = scores.masked_fill(mask == 0, -1e9)
            scores = scores.masked_fill(mask.unsqueeze(1).expand_as(scores) == 0, -1e9)
        p_attn = F.softmax(scores, dim=-1)
        if dropout is not None:
            p_attn = dropout(p_attn)
        return torch.matmul(p_attn, value), p_attn

    def mean_pooling(self, model_output, attention_mask):
        token_embeddings = model_output[0]  # First element of model_output contains all token embeddings
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        return torch.sum(token_embeddings * input_mask_expanded, 1) / \
               torch.clamp(input_mask_expanded.sum(1), min=1e-9)

    def forward(self, query, key, value, mask=None):
        batch_size = query.size(0)
        if mask is not None:
            # Same mask applied to all h heads.
            mask = mask.unsqueeze(1)

        # 1) Do all the linear projections in batch from d_model => h x d_k
        # query, key, value = \
        #     [l(x).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        #      for l, x in zip(self.linears, (query, key, value))]  # torch.Size([2, 4, 1, 128])
        query, key, value = \
            [l(x).view(batch_size, self.num_heads, self.d_k)
             for l, x in zip(self.linears, (query, key, value))]  # torch.Size([2, 4, 1, 128])

        # 2) Apply attention on all the projected vectors in batch.
        x, self.attn_score = self.attention(query, key, value, mask=mask,
                                            dropout=self.dropout)

        # 3) "Concat" using a view and apply a final linear.
        # x = x.transpose(1, 2).contiguous().view(batch_size, -1, self.num_heads * self.d_k)
        x = x.contiguous().view(batch_size, self.num_heads * self.d_k)
        x = self.linears[-1](x)
        # x = torch.sum(x * mask.permute(0, 2, 1), dim=1) / torch.clamp(mask.permute(0, 2, 1).sum(1), min=1e-9)
        # x = nn.Linear(9, 1)(x.permute(0, 2, 1).cpu()).squeeze(-1)
        return x


class PositionwiseFeedForward(nn.Module):
    def __init__(self, d_model, d_ff, dropout=0.1):
        """
        Implements FFN equation.
        """
        super(PositionwiseFeedForward, self).__init__()
        self.w_1 = nn.Linear(d_model, d_ff)
        self.w_2 = nn.Linear(d_ff, d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        return self.w_2(self.dropout(F.relu(self.w_1(x))))


class LayerNorm(nn.Module):
    def __init__(self, size, eps=1e-6):
        """
        Construct a LayerNorm module (See citation for details).
        :param size:
        :param eps:
        """
        super(LayerNorm, self).__init__()
        self.a_2 = nn.Parameter(torch.ones(size))
        self.b_2 = nn.Parameter(torch.zeros(size))
        self.eps = eps

    def forward(self, x):
        mean = x.mean(-1, keepdim=True)
        std = x.std(-1, keepdim=True)
        return self.a_2 * (x - mean) / (std + self.eps) + self.b_2


class ResidualConnection(nn.Module):
    def __init__(self, size, dropout=0.1):
        """
        A residual connection followed by a layer norm.
        Note for code simplicity the norm is first as opposed to last.
        """
        super(ResidualConnection, self).__init__()
        self.norm = LayerNorm(size)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, sublayer):
        # Apply residual connection to any sublayer with the same size
        return x + self.dropout(sublayer(self.norm(x)))


class HuggingBackbone(nn.Module):
    def __init__(self, model_id):
        super(HuggingBackbone, self).__init__()

        self.model_id = model_id
        if model_id == "starencoder":
            from transformers import AutoTokenizer, AutoModelForPreTraining

            self.tokenizer = AutoTokenizer.from_pretrained("/data/xxx/llm_model/starencoder")
            self.model = AutoModelForPreTraining.from_pretrained("/data/xxx/llm_model/starencoder")
            self.tokenizer.pad_token = self.tokenizer.eos_token

        elif model_id == "all-MiniLM-L6-v2":
            from transformers import AutoTokenizer, AutoModel

            self.tokenizer = AutoTokenizer.from_pretrained("/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/"
                                                           "data/pretrained_model/all-MiniLM-L6-v2")
            self.model = AutoModel.from_pretrained("/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/"
                                                   "data/pretrained_model/all-MiniLM-L6-v2")

        elif model_id == "bge-large-en-v1.5":
            from transformers import AutoTokenizer, AutoModel

            self.tokenizer = AutoTokenizer.from_pretrained("/data/xxx/llm_model/bge-large-en-v1.5")
            self.model = AutoModel.from_pretrained("/data/xxx/llm_model/bge-large-en-v1.5")

    def forward(self, x):
        tokenized_inputs = self.tokenizer(x, padding=True, return_tensors="pt")
        input_ids = tokenized_inputs["input_ids"].to(self.model.device)
        attention_mask = tokenized_inputs["attention_mask"].to(self.model.device)
        if input_ids.shape[-1] == 7:
            input_ids = torch.stack([torch.cat((item, torch.zeros(2).cuda()), dim=-1)
                                     for item in input_ids], dim=0).long()
            attention_mask = torch.stack([torch.cat((item, torch.zeros(2).cuda()), dim=-1)
                                          for item in attention_mask], dim=0).long()

        if self.model_id == "starencoder":
            output = self.model(input_ids=input_ids, attention_mask=attention_mask).hidden_states[-1]
        elif self.model_id == "all-MiniLM-L6-v2":
            output = self.model(input_ids=input_ids, attention_mask=attention_mask).last_hidden_state
        elif self.model_id == "bge-large-en-v1.5":
            output = self.model(input_ids=input_ids, attention_mask=attention_mask).last_hidden_state

        return output, attention_mask


class HuggingBackboneV2(nn.Module):
    def __init__(self, model_id):
        super(HuggingBackboneV2, self).__init__()
        self.model_id = model_id
        if model_id == "starencoder":
            self.model = HuggingFaceEmbeddings(model_name="/data/xxx/llm_model/starencoder")
            self.model.client.tokenizer.pad_token = self.model.client.tokenizer.eos_token
            self.device = self.model.client.device

        elif model_id == "codebert-base":
            self.model = HuggingFaceEmbeddings(model_name="/data/xxx/llm_model/codebert-base")
            self.device = self.model.client.device

        elif model_id == "all-MiniLM-L6-v2":
            # self.model = HuggingFaceEmbeddings(model_name="/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/"
            #                                               "data/pretrained_model/all-MiniLM-L6-v2")
            self.model = SentenceTransformer("/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/"
                                             "data/pretrained_model/all-MiniLM-L6-v2")
            self.device = self.model.device
            for param in self.model.parameters():
                param.requires_grad = False

        elif model_id == "bge-large-en-v1.5":
            self.model = HuggingFaceEmbeddings(model_name="/data/xxx/llm_model/bge-large-en-v1.5")
            self.device = self.model.client.device

        elif model_id == "stella_en_400M_v5":
            # self.model = HuggingFaceEmbeddings(model_name="/data/xxx/llm_model/stella_en_400M_v5")
            # self.device = self.model.client.device
            self.model = SentenceTransformer("/data/xxx/llm_model/stella_en_400M_v5", trust_remote_code=True)
            self.device = self.model.device
            for param in self.model.parameters():
                param.requires_grad = False

        elif model_id == "gte-large-en-v1.5":
            # self.model = HuggingFaceEmbeddings(model_name="/data/xxx/llm_model/gte-large-en-v1.5")
            # self.device = self.model.client.device
            self.model = SentenceTransformer("/data/xxx/llm_model/gte-large-en-v1.5", trust_remote_code=True)
            self.device = self.model.device
            for param in self.model.parameters():
                param.requires_grad = False

        elif model_id == "NV-Embed-v2":
            # self.model = HuggingFaceEmbeddings(model_name="/data/xxx/llm_model/gte-large-en-v1.5")
            # self.device = self.model.client.device
            self.model = SentenceTransformer("/data/xxx/llm_model/NV-Embed-v2", trust_remote_code=True)
            self.device = self.model.device
            for param in self.model.parameters():
                param.requires_grad = False

        elif model_id == "stella_en_1.5B_v5":
            # self.model = HuggingFaceEmbeddings(model_name="/data/xxx/llm_model/gte-large-en-v1.5")
            # self.device = self.model.client.device
            self.model = SentenceTransformer("/data/xxx/llm_model/stella_en_1.5B_v5", trust_remote_code=True)
            self.device = self.model.device
            for param in self.model.parameters():
                param.requires_grad = False

    def forward(self, x):
        if self.model_id == "starencoder":
            embeddings = torch.Tensor(self.model.embed_documents(x)).to(self.device)  # torch.Size([2, 768])

        if self.model_id == "codebert-base":
            embeddings = torch.Tensor(self.model.embed_documents(x)).to(self.device)

        elif self.model_id == "all-MiniLM-L6-v2":
            embeddings = torch.Tensor(self.model.encode(x)).to(self.device)  # torch.Size([2, 384])

        elif self.model_id == "bge-large-en-v1.5":
            embeddings = torch.Tensor(self.model.embed_documents(x)).to(self.device)  # torch.Size([2, 1024])

        elif self.model_id == "stella_en_400M_v5":
            # embeddings = torch.Tensor(self.model.embed_documents(x)).to(self.device)
            embeddings = torch.Tensor(self.model.encode(x)).to(self.device)

        elif self.model_id == "gte-large-en-v1.5":
            # embeddings = torch.Tensor(self.model.embed_documents(x)).to(self.device)
            embeddings = torch.Tensor(self.model.encode(x)).to(self.device)

        elif self.model_id == "NV-Embed-v2":
            # embeddings = torch.Tensor(self.model.embed_documents(x)).to(self.device)
            embeddings = torch.Tensor(self.model.encode(x)).to(self.device)

        elif self.model_id == "stella_en_1.5B_v5":
            # embeddings = torch.Tensor(self.model.embed_documents(x)).to(self.device)
            embeddings = torch.Tensor(self.model.encode(x)).to(self.device)

        return embeddings, None


class CodeDescEmbedding(nn.Module):
    def __init__(self, input_sizes, hidden_size,
                 num_experts=2, num_heads=4, dropout=0.05):
        super().__init__()

        # Code Backbone
        self.code = HuggingBackboneV2(model_id="starencoder")
        # self.code = HuggingBackboneV2(model_id="codebert-base")

        # NL Backbone
        self.desc1 = HuggingBackboneV2(model_id="all-MiniLM-L6-v2")
        self.desc2 = HuggingBackboneV2(model_id="bge-large-en-v1.5")

        self.dropout = nn.Dropout(p=dropout)
        self.expert_kernels = nn.ModuleList([nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.BatchNorm1d(hidden_size),
            nn.LeakyReLU()
        ) for input_size in input_sizes])

        # one gate
        self.gate_kernel = nn.Sequential(
            nn.Linear(input_sizes[-1], hidden_size),
            nn.LeakyReLU(),
            nn.Linear(hidden_size, num_experts),
            nn.LeakyReLU()
        )

        self.attn = MultiHeadAttention(hidden_size, num_heads=num_heads, dropout=dropout)
        self.residual = nn.ModuleList([ResidualConnection(hidden_size,
                                                          dropout=dropout) for _ in range(num_experts + 1)])

        self.apply(self.init_weights)

    def forward(self, keyword, description):
        # Code
        code, code_mask = self.code(keyword)
        code = self.expert_kernels[0](code)  # torch.Size([2, 512])

        # Description
        desc1, desc1_mask = self.desc1(description)
        desc2, desc2_mask = self.desc2(description)

        # expert_outputs = [self.residual[0](desc1, self.expert_kernels[1]),
        #                   self.residual[1](desc2, self.expert_kernels[2])]
        expert_outputs = [self.expert_kernels[1](desc1),
                          self.expert_kernels[2](desc2)]  # torch.Size([2, 512])

        expert_outputs = torch.stack(expert_outputs, 0)  # torch.Size([2, 2, 512])
        expert_outputs = expert_outputs.permute(1, 2, 0)  # torch.Size([2, 512, 2])
        # expert_outputs = expert_outputs.permute(1, 2, 3, 0)  # torch.Size([2, 512, 2])

        # gate_output = self.gate_kernel(desc2[:, -1, :])
        gate_output = self.gate_kernel(desc2)  # torch.Size([2, 2])
        gate_output = nn.Softmax(dim=-1)(gate_output)  # torch.Size([2, 2])
        # gate_batch_sum = torch.sum(gate_output, dim=0)

        expanded_gate_output = gate_output.unsqueeze(1)  # torch.Size([2, 1, 2])
        # expanded_gate_output = gate_output.unsqueeze(1).unsqueeze(1)
        weighted_expert_output = expert_outputs * expanded_gate_output.expand_as(
            expert_outputs)  # torch.Size([2, 512, 2])
        desc = torch.sum(weighted_expert_output, dim=-1)  # torch.Size([2, 512])

        # Aggregator
        desc = self.attn(code, desc, desc, mask=desc1_mask)
        # desc = self.attn(desc, code, code, mask=code_mask)
        # desc = self.residual[-1](desc, nn.Identity(desc_attn))
        return desc

    def init_weights(self, module):
        """ Initialize the weights.
        """
        if isinstance(module, (nn.Linear, nn.Embedding)):
            module.weight.data.normal_(mean=0.0, std=0.02)
        if isinstance(module, nn.Linear) and module.bias is not None:
            module.bias.data.zero_()

    def embed_query(self, query):
        # keyword, description = eval(query)["keyword"], eval(query)["description"]
        keyword, description = query.split("--separator--")
        embedding = self.forward([keyword], [description]).squeeze(0).tolist()
        return embedding

    def embed_documents(self, texts):
        embeddings = list()
        for text in texts:
            # keyword, description = eval(text)["keyword"], eval(text)["description"]
            keyword, description = text.split("--separator--")
            embedding = self.forward([keyword], [description]).squeeze(0).tolist()
            embeddings.append(embedding)
        return embeddings


class MultiEmbedding(SentenceTransformer):
    def __init__(self):
        super(MultiEmbedding, self).__init__()
        self.model1 = SentenceTransformer("/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/"
                                          "data/pretrained_model/all-MiniLM-L6-v2")
        self.model2 = HuggingFaceEmbeddings(model_name="/data/xxx/llm_model/bge-large-en-v1.5")
        # self.model3 = HuggingFaceEmbeddings(model_name="/data/xxx/llm_model/codebert-base")
        # self.model4 = HuggingFaceEmbeddings(model_name="/data/xxx/llm_model/starencoder")
        # self.model4.tokenizer.pad_token = self.model4.tokenizer.eos_token
        # self.model4.client.tokenizer.pad_token = self.model4.client.tokenizer.eos_token

    def forward(self, texts):
        return torch.Tensor([self.model1.encode(t).tolist() +
                             self.model2.embed_query(t) for t in texts]), None

    def embed_query(self, query):
        # return torch.ones(100, dtype=torch.int).tolist()
        return self.model1.encode(query).tolist() + self.model2.embed_query(query)

    def embed_documents(self, texts):
        # return [torch.ones(100, dtype=torch.int).tolist() for _ in texts]
        return [self.model1.encode(t).tolist() + self.model2.embed_query(t) for t in texts]


class RetrievalModel:
    def __init__(self, model_id):
        self.model_id = model_id

    def retrieve(self, query, vector_db, top_k=None):
        if self.model_id == "BM25":
            # results = vector_db.invoke(query)
            # results = vector_db.get_relevant_documents(query)
            results = vector_db.retrieve(query)
        else:
            results = vector_db.similarity_search_with_score(query=query, k=top_k)
            # results = vector_db.similarity_search_with_relevance_scores(query=query, k=top_k)
            # vector_db.similarity_search_with_relevance_scores(query=query, k=top_k, filter={"Function": "="})

        return results
