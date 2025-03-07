# CrackSQL

<p align="center">
  <b>Unlock seamless SQL translation – effortless, precise, and efficient across databases</b>
</p>

<p align="center">
  <a>![Dialect](https://img.shields.io/badge/Dialect%20Pair-6-blue?style=flat-square)</a>
  <a>![Benchmark](https://img.shields.io/badge/Translation%20Benchmark-501-blue?style=flat-square)</a>
  <a>![LLM](https://img.shields.io/badge/Finetuned%20LLM-4-green?style=flat-square)</a>
  <a>![Embedding Model](https://img.shields.io/badge/Finetuned%20Embedding%20Model-3-green?style=flat-square)</a>
</p>

<p align="center">
  <a href="#-demo">Demo</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-feature-extension">Feature Extension</a> • 
  <a href="#-faq">FAQ</a> •  
  <a href="#-community">Community</a> •  
  <a href="#-contributors">Contributors</a> •  
  <a href="#-license">License</a>
</p>
<p align="center">
  <b>English</b> | <a href="./README_ZH.md">简体中文</a>
</p>

<div style="text-align: center;">
  <p style="padding: 10px; background-color: #f9f9f9; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); display: inline-block;">
    <span style="color: black;"><b>Star ⭐ and subscribe 🔔 for the latest features and improvements!</b></span>
  </p>
</div>

## ✨ Project Introduction

CrackSQL is a powerful SQL dialect translation tool that integrates rule-based strategies with LLMs for high accuracy.
It enables seamless conversion between dialects (e.g., PostgreSQL to MySQL) with flexible access through Python API, command line, and web interface.

> - **03/2025:** We have refactored the code and released our project across multiple open-source platforms ([PyPI](https://pypi.org/project/cracksql/0.0.0b0/)). We are currently working on [new features](#todo) and more contributors are welcomed! :wave: 👫
> - **02/2025:** Our paper "*Cracking SQL Barrier: An LLM-based Dialect Translation System*" has been accepted by SIGMOD 2025! :tada: :tada: :tada:

## 📚 Features

- 🚀 **Extensive Dialect Compatibility**: Effortlessly translates between PostgreSQL, MySQL, and Oracle with flexible, tailored strategies.
- 🎯 **Precision & Advanced Processing**: Achieves flawless translations with function-oriented query handling and cutting-edge model-based syntax matching through an adaptive local-to-global iteration strategy.
- 🔄 **Versatile Access & Integration**: Seamlessly integrates with Python API, command line, and web interface to meet all user requirements.

## 📊 Performance

Translation Accuracy (%) of Different Methods (N/A denotes the dialect translation is not supported in Ora2Pg).
Note that the required translation duration is highly dependent on the SQL complexity (e.g., the number of SQL syntax piece to be translated) and can vary from several seconds to minutes.

| **Method**                 | **PG → MySQL** | **MySQL → PG** | **PG → Oracle** | **Oracle → PG** | **MySQL → Oracle** | **Oracle → MySQL** |
|--------------------------------------------------|:---------------------------------------------------:|:---------------------------------------------------:|:----------------------------------------------------:|:----------------------------------------------------:|:-------------------------------------------------------:|:-------------------------------------------------------:|
|                                                  | **Acc_EX**                                 | **Acc_RES**                                | **Acc_EX**                                  | **Acc_RES**                                 | **Acc_EX**                                     | **Acc_RES**                                    |
| **SQLGlot**                  | 74.19                                               | 70.97                                               | 60.32                                                | 60.32                                                | 55.81                                                   | 53.49                                                   |
| **jOOQ**                          | 70.97                                               | 70.97                                               | 39.68                                                | 39.68                                                | 62.79                                                   | 60.47                                                   |
| **Ora2Pg** | N/A                                        | N/A                                        | 33.33                                     | 33.33                                     | N/A                                            | N/A                                            |
| **SQLines**                  | 9.68                                                | 9.68                                                | 31.75                                                | 31.75                                                | 53.49                                                   | 48.84                                                   |
| **GPT-4o**                     | 61.29                                               | 61.29                                               | 50.79                                                | 44.44                                                | 60.47                                                   | 55.81                                                   |
| **CrackSQL (Ours)**                          | **87.1**                                       | **74.19**                                      | **85.71**                                       | **79.37**                                       | **69.77**                                          | **67.44**                                          |


## 🖥️ Demo

- Homepage of the deployed translation service:

![Web Interface Homepage](./data/images/home.png)

- Detailed translation process of specific translation pair:

![Web Interface Rewrite Detail](./data/images/detail.png)

## 🚀 Quick Start

### Method 1: PyPI Package Installation

Install the PyPI package at the [official website](https://pypi.org/project/cracksql/0.0.0b0/).

![Web Interface Preview](./data/images/pypi.png)

```
# create virtual environment
conda create -n CrackSQL python=3.10
conda activate CrackSQL

# install PyPI package
pip install cracksql==0.0.0b0
```

An running code example using this PyPI package is below:

```python

from cracksql.cracksql import translate, initkb

def initkb_func():
    try:
        initkb("./init_config.yaml")
        print("Knowledge base initialized successfully")
    except Exception as e:
        print(f"Knowledge base initialization failed: {str(e)}")
        import traceback
        traceback.print_exc()


def trans_func():

    target_db_config = {
        "host": "target database host",
        "port": target database number (int type),
        "user": "target database username",
        "password": "target database password",
        "db_name": "target database database name"
    }

    vector_config = {
        "src_kb_name": "source database knowledge base name",
        "tgt_kb_name": "target database knowledge base name"
    }

    try:
        print("Starting SQL translation...")
        translated_sql, model_ans_list, used_pieces, lift_histories = translate(
            model_name="DeepSeek-R1-Distill-Qwen-32B", 
            src_sql='SELECT DISTINCT "t1"."id" , EXTRACT(YEAR FROM CURRENT_TIMESTAMP) - EXTRACT(YEAR FROM CAST( "t1"."birthday" AS TIMESTAMP )) FROM "patient" AS "t1" INNER JOIN "examination" AS "t2" ON "t1"."id" = "t2"."id" WHERE "t2"."rvvt" = "+"',
            src_dialect="postgresql",
            tgt_dialect="mysql",
            target_db_config=target_db_config,
            vector_config=vector_config,
            out_dir="./", 
            retrieval_on=False, 
            top_k=3
        )

        print("Translation completed!")
        print(f"Translated SQL: {translated_sql}")
        print(f"Model answer list: {model_ans_list}")
        print(f"Used knowledge pieces: {used_pieces}")
        print(f"Lift histories: {lift_histories}")
    except Exception as e:
        print(f"Error occurred during translation: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":

    initkb_func()
    trans_func()

```

### Method 2: Source Code Installation

#### 1. Clone Repository

```bash
git clone https://github.com/weAIDB/CrackSQL.git
```

#### 2. Use Frontend and Backend Application

```bash
# Start backend
cd CrackSQL/backend

# Install dependencies
conda create -n CrackSQL python=3.10
conda activate CrackSQL
pip install -r requirements.txt

# Initialize database
flask db init      # Initialize
flask db migrate   # Generate version file
flask db upgrade   # Synchronize to database

# Initialize knowledge base (Optional, can be done manually in the frontend after starting the frontend project)
# 1. First rename config/init_config.yaml.copy to config/init_config.yaml
# 2. Modify the relevant information in config/init_config.yaml. If you want to initialize the knowledge base, Embedding Model is required
python3 init_knowledge_base.py --init_all

# Start backend service (The backend service port can also be modified in app.py, currently 30006)
python app.py

# Start frontend (requires nodejs, version 20.11.1+)
cd CrackSQL/webui

# Install dependencies
yarn cache clean
yarn install

# Start development server
yarn dev

# Visit http://localhost:50212 to use the Web interface

# Tips: 
# If you want to modify the frontend port number, you can modify it in webui/vite.config.js: port: 50212
# If the backend API port number has been changed, or you want to use the server's IP, you can modify the VITE_APP_BASE_URL parameter in webui/.env.serve-dev file (if the file does not exist, you can rename webui/.env.serve-dev_copy to .env.serve-dev).
```

#### 3. Command Line Usage

```bash
# Initialize knowledge base (Optional, can be done manually in the frontend after starting the frontend project)
# 1. First rename config/init_config.yaml.copy to config/init_config.yaml
# 2. Modify the relevant information in config/init_config.yaml. If you want to initialize the knowledge base, Embedding Model is required
python init_knowledge_base.py --init_all

# Convert
python translate.py --src_dialect "source dialect"
```

## 📎 Feature Extension

### Add New Syntax

<i>To be supplemented</i>

### Add New Database

<i>Start from scratch</i>

### Fine-tune Vector Model

<i>To be supplemented</i>

## 🤔 FAQ

<i>TODO: Add frequently asked questions</i>

## 📋 TODO <a id="todo"></a>

- Python API

## 👫 Community

Welcome to scan the QR code to join the WeChat group!

<p align="center">
  <i>TODO: Add WeChat group QR code</i>
</p>

## 📒 Citation

If you like this project, please cite our paper:

```
@misc{zhou2025cracksql,
      title={Cracking SQL Barriers: An LLM-based Dialect Transaltion System}, 
      author={Wei Zhou, Yuyang Gao, Xuanhe Zhou, and Guoliang Li},
      year={2025},
      journal={Proc. {ACM} Manag. Data},
      volume={3},
      number={2},
}
```

## 📧 Contributors

<a href="https://github.com/code4DB/CrackSQL/network/dependencies">
  <img src="https://contrib.rocks/image?repo=code4DB/CrackSQL" />
</a>

## 📝 License

<i>TODO: Add open source license</i>

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

