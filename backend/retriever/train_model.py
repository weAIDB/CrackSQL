# -*- coding: utf-8 -*-
# @Project: xxxx
# @Module: train_model
# @Author: xxxx
# @Time: 2024/9/15 17:41

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1"

import json
import random
import logging
from tqdm import tqdm

import torch
import torch.nn as nn
from torch.utils.tensorboard import SummaryWriter
from torch.utils.data import DataLoader, random_split
from torch.optim.lr_scheduler import ReduceLROnPlateau

import sys
sys.path.append("/data/xxxx/index/sql_convertor/LLM4DB")

from CrackSQL.utils import tools
from CrackSQL.retriever.retriever_dataset import CrossLingualDataset
from CrackSQL.retriever.retrieval_model import CodeDescEmbedding, ContrastiveLossV2

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

category = "func"  # func, type, keyword


def train(args, train_loader, valid_loader):
    model = CodeDescEmbedding(input_sizes=(768, 384, 1024, 1024), hidden_size=512,
                              num_experts=2, num_heads=4, dropout=0.05)
    criterion = ContrastiveLossV2(temperature=0.08)
    optimizer = torch.optim.Adam(model.parameters(), args.lr)
    scheduler = ReduceLROnPlateau(optimizer, "min", factor=0.5,
                                  patience=6, min_lr=1e-5, verbose=True)

    if torch.cuda.is_available():
        model = torch.nn.DataParallel(model)
        model.cuda()

    model = model.to(device)
    criterion = criterion.to(device)
    for epoch in tqdm(range(1, args.epoch + 1)):

        logging.info(f"The `lr` of EP{epoch} is `{optimizer.param_groups[0]['lr']}`.")

        model.train()
        total_loss = 0
        pro_bar = tqdm(enumerate(train_loader))
        for bi, batch in pro_bar:
            pro_bar.set_description(f"Epoch [{epoch} / {args.epoch}]")

            keywords = [item["KEYWORD"][0] for item in batch[0]]
            descriptions = [item["DESC"][0] for item in batch[0]]
            pos_indices = torch.LongTensor([(item[0][0], item[1][0]) for item in batch[1]])

            embeddings = model(keywords, descriptions)
            loss = criterion(embeddings, pos_indices)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
            pro_bar.set_postfix(train_loss=total_loss / (bi + 1))

            tools.add_summary_value("train loss", loss.item())
            tools.tf_step += 1
            if tools.tf_step % 100 == 0:
                tools.summary_writer.flush()
        logging.info(f"The final train loss of EP{epoch} is: {total_loss / (bi + 1)}.")

        model.eval()
        total_loss = 0
        pro_bar = tqdm(enumerate(valid_loader))
        for bi, batch in pro_bar:
            pro_bar.set_description(f"Epoch [{epoch}/{args.epoch}]")

            keywords = [item["KEYWORD"][0] for item in batch[0]]
            descriptions = [item["DESC"][0] for item in batch[0]]
            pos_indices = torch.LongTensor([(item[0][0], item[1][0]) for item in batch[1]])

            embeddings = model(keywords, descriptions)
            loss = criterion(embeddings, pos_indices)

            total_loss += loss.item()
            pro_bar.set_postfix(valid_loss=total_loss / (bi + 1))

            tools.add_summary_value("valid loss", loss.item())
            tools.tf_step += 1
            if tools.tf_step % 100 == 0:
                tools.summary_writer.flush()

        scheduler.step(total_loss / (bi + 1))

        logging.info(f"The final valid loss of EP{epoch} is: {total_loss / (bi + 1)}.")

        model_state_dict = model.state_dict()
        model_source = {
            "settings": args,
            "model": model_state_dict,
        }
        if epoch % args.model_save_gap == 0:
            model_save = args.model_save.format(args.exp_id, category + str(epoch))
            if not os.path.exists(os.path.dirname(model_save)):
                os.makedirs(os.path.dirname(model_save))
            torch.save(model_source, model_save)


if __name__ == "__main__":
    parser = tools.get_parser()
    args = parser.parse_args()

    random.seed(args.seed)
    torch.manual_seed(args.seed)
    logging.info(f"Set the random seed = `{args.seed}`.")

    tools.summary_writer = SummaryWriter(args.logdir.format(args.exp_id))
    tools.summary_writer.add_text(
        "parameters",
        "|param|value|\n|-|-|\n%s" % ("\n".join([f"|{key}|{value}|" for key, value in vars(args).items()])),
        0
    )
    logging.info(f"Set the tensorboard logdir = `{args.logdir.format(args.exp_id)}`.")

    data_load = "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/" \
                "processed_document/three_dialects_built-in-function_coarse.json"
    data_load = f"/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/" \
                f"processed_document/three_dialects_{category}_fine.json"
    with open(data_load, "r") as rf:
        data_raw = json.load(rf)

    # 64 * 20 -> 64 * 5
    dataset = CrossLingualDataset(data_raw=data_raw, data_num=64 * 2,
                                  batch_size=64, seed=666, category=category)
    train_set, valid_set = random_split(dataset, [int(0.8 * len(dataset)),
                                                  len(dataset) - int(0.8 * len(dataset))])

    train_loader = DataLoader(dataset=train_set, batch_size=1, shuffle=True, drop_last=True)
    valid_loader = DataLoader(dataset=valid_set, batch_size=1, shuffle=True, drop_last=True)

    train(args, train_loader, valid_loader)
