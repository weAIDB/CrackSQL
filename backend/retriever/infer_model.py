# -*- coding: utf-8 -*-
# @Project: xxxx
# @Module: infer_model
# @Author: xxxx
# @Time: 2024/9/15 17:42

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1"

import json
from tqdm import tqdm

import torch
from torch.utils.data import DataLoader

from CrackSQL.retriever.retrieval_model import CodeDescEmbedding, ContrastiveLossV2, HuggingBackboneV2
from CrackSQL.retriever.retriever_dataset import CrossLingualDataset

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def infer():
    data_load = "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/" \
                "processed_document/three_dialects_built-in-function_coarse.json"
    with open(data_load, "r") as rf:
        data_raw = json.load(rf)

    dataset = CrossLingualDataset(data_raw=data_raw, data_num=6, batch_size=64, seed=999)
    data_loader = DataLoader(dataset=dataset, batch_size=1, shuffle=True, drop_last=True)

    criterion = ContrastiveLossV2(temperature=0.08).to(device)

    model_bge = HuggingBackboneV2(model_id="bge-large-en-v1.5")
    model_random = CodeDescEmbedding(input_sizes=(768, 384, 1024, 1024), hidden_size=512,
                                     num_experts=2, num_heads=4, dropout=0.05).to(device)
    model_trained = CodeDescEmbedding(input_sizes=(768, 384, 1024, 1024), hidden_size=512,
                                      num_experts=2, num_heads=4, dropout=0.05).to(device)
    model_trained = torch.nn.DataParallel(model_trained)

    model_load = "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/" \
                 "retriever/exp_res/exp_pre_bak/model/rewrite_Train_1.pt"
    model_source = torch.load(model_load, map_location=device)
                              # map_location=lambda storage, loc: storage)

    model_trained.load_state_dict(model_source["model"])
    model_trained.eval()

    pro_bar = tqdm(enumerate(data_loader))
    for bi, batch in pro_bar:
        keywords = [item["Function"][0] for item in batch[0]]
        descriptions = [item["Description"][0] for item in batch[0]]
        pos_indices = torch.LongTensor([(item[0][0], item[1][0]) for item in batch[1]])

        embeddings_bge = model_bge(descriptions)[0]
        embeddings_random = model_random(keywords, descriptions)
        embeddings_trained = model_trained(keywords, descriptions)

        loss_bge = criterion(embeddings_bge, pos_indices)
        loss_random = criterion(embeddings_random, pos_indices)
        loss_trained = criterion(embeddings_trained, pos_indices)

        print(f"loss_bge: {loss_bge}; loss_random: {loss_random}; loss_trained: {loss_trained}.")


if __name__ == "__main__":
    infer()
