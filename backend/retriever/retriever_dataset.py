# -*- coding: utf-8 -*-
# @Project: xxxx
# @Module: retriever_dataset
# @Author: xxxx
# @Time: 2024/9/17 19:42

import random
import re

from torch.utils.data import Dataset


class CrossLingualDataset(Dataset):
    def __init__(self, data_raw, data_num, batch_size, seed=666, category=None):
        self.data_raw = data_raw
        self.data_num = data_num
        self.batch_size = batch_size
        self.seed = seed
        self.category = category

        self.data = list()
        if self.category == "func":
            self.make_data_function()
        elif self.category == "keyword":
            self.make_data_keyword()
        elif self.category == "type":
            self.make_data_type()

    def make_data_function(self):
        random.seed(self.seed)
        for _ in range(self.data_num):
            current_size = 0
            selected = list()
            while current_size < self.batch_size:
                key = random.choice(range(len(self.data_raw)))

                if len(self.data_raw[key]) == 1:
                    continue

                if current_size + len(self.data_raw[key]) > self.batch_size:
                    selected.append(random.sample(self.data_raw[key], k=self.batch_size - current_size))
                else:
                    selected.append(self.data_raw[key])
                current_size += len(self.data_raw[key])

            selected_pre = list()
            for no, li in enumerate(selected):
                for item in li:
                    item["Label"] = no

                    if item["Dialect"] == "postgres":
                        item["KEYWORD"] = list()
                        for field in ["Name", 'Argument Type', 'Argument Type(s)',
                                      'Aggregated Argument Type(s)',
                                      'Direct Argument Type(s)', 'Return Type']:
                            content = item.get(field, "")
                            if isinstance(content, list):
                                item["KEYWORD"].extend(content)
                            else:
                                item["KEYWORD"].append(content)
                        item["KEYWORD"] = "<sep>".join(item["KEYWORD"])

                        item["DESC"] = list()
                        for field in ['Description', 'Example', 'Result',
                                      'Example Query', 'Example Result',
                                      'compensate']:
                            content = item.get(field, "")
                            if isinstance(content, list):
                                item["DESC"].extend(content)
                            else:
                                item["DESC"].append(content)
                        item["DESC"] = "<sep>".join(item["DESC"])

                    elif item["Dialect"] == "mysql":
                        item["KEYWORD"] = list()
                        for field in ["Name"]:
                            content = item.get(field, "")
                            if isinstance(content, list):
                                item["KEYWORD"].extend(content)
                            else:
                                item["KEYWORD"].append(content)
                        item["KEYWORD"] = "<sep>".join(item["KEYWORD"])

                        item["DESC"] = list()
                        for field in ['Description', 'Demo', 'Detail']:
                            content = item.get(field, "")
                            if isinstance(content, list):
                                item["DESC"].extend(content)
                            else:
                                item["DESC"].append(content)
                        item["DESC"] = "<sep>".join(item["DESC"])

                    elif item["Dialect"] == "oracle":
                        item["KEYWORD"] = list()
                        for field in ["Name"]:
                            content = item.get(field, "")
                            if isinstance(content, list):
                                item["KEYWORD"].extend(content)
                            else:
                                item["KEYWORD"].append(content)
                        item["KEYWORD"] = "<sep>".join(item["KEYWORD"])

                        item["DESC"] = list()
                        for field in ['Description']:
                            content = item.get(field, "")
                            if isinstance(content, list):
                                item["DESC"].extend(content)
                            else:
                                item["DESC"].append(content)
                        item["DESC"] = "<sep>".join(item["DESC"])

                    selected_pre.append(item)

            random.shuffle(selected_pre)

            pos_indices = list()
            for i in range(len(selected_pre)):
                for j in range(i + 1, len(selected_pre)):
                    if selected_pre[i]["Label"] == selected_pre[j]["Label"]:
                        pos_indices.append((i, j))
                        pos_indices.append((j, i))
            pos_indices = sorted(pos_indices)

            self.data.append((selected_pre, pos_indices))

    def make_data_keyword(self):
        random.seed(self.seed)
        for _ in range(self.data_num):
            current_size = 0
            selected = list()
            while current_size < self.batch_size:
                key = random.choice(list(self.data_raw))

                if len(self.data_raw[key]) == 1:
                    continue

                if current_size + len(self.data_raw[key]) > self.batch_size:
                    selected.append(random.sample(self.data_raw[key], k=self.batch_size - current_size))
                else:
                    selected.append(self.data_raw[key])
                current_size += len(self.data_raw[key])

            selected_pre = list()
            for no, li in enumerate(selected):
                for item in li:
                    if "Count" in item.keys():
                        item.pop("Count")

                    item["Label"] = no

                    if item["Dialect"] == "postgres":
                        item["KEYWORD"] = list()
                        for field in ['Name']:
                            content = item.get(field, "")
                            if isinstance(content, list):
                                item["KEYWORD"].extend(content)
                            else:
                                item["KEYWORD"].append(str(content))
                        item["KEYWORD"] = "<sep>".join(map(str, item["KEYWORD"]))

                        item["DESC"] = list()
                        for field in ['Description', 'Demo']:
                            content = item.get(field, "")
                            if isinstance(content, list):
                                item["DESC"].extend(content)
                            else:
                                item["DESC"].append(str(content))
                        item["DESC"] = "<sep>".join(map(str, item["DESC"]))

                    elif item["Dialect"] == "mysql":
                        item["KEYWORD"] = list()
                        for field in ["Name"]:
                            content = item.get(field, "")
                            if isinstance(content, list):
                                item["KEYWORD"].extend(content)
                            else:
                                item["KEYWORD"].append(str(content))
                        item["KEYWORD"] = "<sep>".join(map(str, item["KEYWORD"]))

                        item["DESC"] = list()
                        for field in ['Description', 'Demo', 'Detail']:
                            content = item.get(field, "")
                            if isinstance(content, list):
                                item["DESC"].extend(content)
                            else:
                                item["DESC"].append(str(content))
                        item["DESC"] = "<sep>".join(map(str, item["DESC"]))

                    elif item["Dialect"] == "oracle":
                        item["KEYWORD"] = list()
                        for field in ["Name"]:
                            content = item.get(field, "")
                            if isinstance(content, list):
                                item["KEYWORD"].extend(content)
                            else:
                                item["KEYWORD"].append(str(content))
                        item["KEYWORD"] = "<sep>".join(map(str, item["KEYWORD"]))

                        item["DESC"] = list()
                        for field in ['Description', 'Demo']:
                            content = item.get(field, "")
                            if isinstance(content, list):
                                item["DESC"].extend(content)
                            else:
                                item["DESC"].append(str(content))
                        item["DESC"] = "<sep>".join(map(str, item["DESC"]))

                    selected_pre.append(item)

            random.shuffle(selected_pre)

            pos_indices = list()
            for i in range(len(selected_pre)):
                for j in range(i + 1, len(selected_pre)):
                    if selected_pre[i]["Label"] == selected_pre[j]["Label"]:
                        pos_indices.append((i, j))
                        pos_indices.append((j, i))
            pos_indices = sorted(pos_indices)

            self.data.append((selected_pre, pos_indices))

    def make_data_type(self):
        random.seed(self.seed)
        for _ in range(self.data_num):
            current_size = 0
            selected = list()
            while current_size < self.batch_size:
                key = random.choice(list(self.data_raw))

                if len(self.data_raw[key]) == 1:
                    continue

                if current_size + len(self.data_raw[key]) > self.batch_size:
                    selected.append(random.sample(self.data_raw[key], k=self.batch_size - current_size))
                else:
                    selected.append(self.data_raw[key])
                current_size += len(self.data_raw[key])

            selected_pre = list()
            for no, li in enumerate(selected):
                for item in li:
                    item["Label"] = no

                    if item["Dialect"] == "postgres":
                        item["KEYWORD"] = list()
                        for field in ['Name']:
                            content = item.get(field, "")
                            if isinstance(content, list):
                                item["KEYWORD"].extend(content)
                            else:
                                item["KEYWORD"].append(content)
                        item["KEYWORD"] = "<sep>".join(item["KEYWORD"])

                        item["DESC"] = list()
                        for field in ['Description', 'Storage Size', 'Range',
                                      'Low Value', 'High Value', 'Compensate']:
                            content = item.get(field, "")
                            if isinstance(content, list):
                                item["DESC"].extend(content)
                            else:
                                item["DESC"].append(content)
                        item["DESC"] = "<sep>".join(item["DESC"])

                    elif item["Dialect"] == "mysql":
                        item["KEYWORD"] = list()
                        for field in ["Name"]:
                            content = item.get(field, "")
                            if isinstance(content, list):
                                item["KEYWORD"].extend(content)
                            else:
                                item["KEYWORD"].append(content)
                        item["KEYWORD"] = "<sep>".join(item["KEYWORD"])

                        item["DESC"] = list()
                        for field in ['Description', 'Storage (Bytes)',
                                      'Minimum Value Signed', 'Maximum Value Signed', 'Compensate']:
                            content = item.get(field, "")
                            if isinstance(content, list):
                                item["DESC"].extend(content)
                            else:
                                item["DESC"].append(content)
                        item["DESC"] = "<sep>".join(item["DESC"])

                    elif item["Dialect"] == "oracle":
                        item["KEYWORD"] = list()
                        for field in ["Type"]:
                            content = item.get(field, "")
                            if isinstance(content, list):
                                item["KEYWORD"].extend(content)
                            else:
                                item["KEYWORD"].append(content)
                        item["KEYWORD"] = "<sep>".join(item["KEYWORD"])

                        item["DESC"] = list()
                        for field in ['Description']:
                            content = item.get(field, "")
                            if isinstance(content, list):
                                item["DESC"].extend(content)
                            else:
                                item["DESC"].append(content)
                        item["DESC"] = "<sep>".join(item["DESC"])

                    selected_pre.append(item)

            random.shuffle(selected_pre)

            pos_indices = list()
            for i in range(len(selected_pre)):
                for j in range(i + 1, len(selected_pre)):
                    if selected_pre[i]["Label"] == selected_pre[j]["Label"]:
                        pos_indices.append((i, j))
                        pos_indices.append((j, i))
            pos_indices = sorted(pos_indices)

            self.data.append((selected_pre, pos_indices))

    def make_data_v1(self):
        random.seed(self.seed)
        for _ in range(self.data_num):
            current_size = 0
            selected = list()
            while current_size < self.batch_size:
                key = random.choice(list(self.data_raw))
                if current_size + len(self.data_raw[key]) > self.batch_size:
                    selected.append(random.sample(list(self.data_raw[key]), k=self.batch_size - current_size))
                else:
                    selected.append(self.data_raw[key])
                current_size += len(self.data_raw[key])

            selected_pre = list()
            for no, li in enumerate(selected):
                for item in li:
                    item["Label"] = no
                    selected_pre.append(item)

            random.shuffle(selected_pre)

            pos_indices = list()
            for i in range(len(selected_pre)):
                for j in range(i + 1, len(selected_pre)):
                    if selected_pre[i]["Label"] == selected_pre[j]["Label"]:
                        pos_indices.append((i, j))
                        pos_indices.append((j, i))
            pos_indices = sorted(pos_indices)

            self.data.append((selected_pre, pos_indices))

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)
