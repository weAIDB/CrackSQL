# CrackSQL

<p align="center">
  <b>A powerful SQL dialect conversion tool that supports precise conversion between different SQL dialects</b>
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
  <b>English</b> | <a href="./README_CH.md">简体中文</a>
</p>

<p align="center">
  <b>Star ⭐ and subscribe 🔔 for the newest features and improvements!</b>
</p>

## ✨ Project Introduction

CrackSQL is a tool focused on SQL dialect conversion, supporting precise conversion between different SQL dialects (such
as PostgreSQL to MySQL). It provides three usage methods: command line, Python API, and Web interface, meeting the needs
of different scenarios.

> - **03/2025:** We have refactored the code and released our project across multiple open-source platforms ([PyPI](https://pypi.org/project/cracksql/0.0.0b0/)). We are currently working on new features and more contributors are welcomed! :wave: 👫
> - **02/2025:** Our paper "*Cracking SQL Barrier: An LLM-based Dialect Translation System*" has been accepted by SIGMOD 2025! :tada: :tada: :tada:

## 📚 Features

- 🚀 **Multi-dialect Support**: Supports conversion between three mainstream database dialects: PostgreSQL, MySQL, and
  Oracle
- 🎯 **High-precision Conversion**: Based on a three-layer conversion architecture to ensure the accuracy of conversion
  results
- 🌟 **Multiple Usage Methods**: Supports command line, Python API, and Web interface
- 🔍 **Function-oriented Syntax Processing**: Breaks down SQL statements into syntax elements for specific functions
- 🧠 **Model-based Syntax Matching**: Uses innovative cross-dialect embedding models for conversion
- 🔄 **Local to Global Conversion Strategy**: Flexibly handles complex SQL conversion scenarios

## 📊 Performance

Translation Accuracy (%) of Different Methods (N/A denotes the dialect translation is not supported in Ora2Pg).
Note that the translation overhead is highly dependent on the SQL complexity (e.g., the number of SQL syntax piece to be translated) and can vary in several seconds to minutes.

| **Method**                 | **PG → MySQL** | **MySQL → PG** | **PG → Oracle** | **Oracle → PG** | **MySQL → Oracle** | **Oracle → MySQL** |
|--------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|------------------------------------------------------|------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|
|                                                  | **Acc_EX**                                 | **Acc_RES**                                | **Acc_EX**                                  | **Acc_RES**                                 | **Acc_EX**                                     | **Acc_RES**                                    | **Acc_EX** | **Acc_RES** | **Acc_EX** | **Acc_RES** | **Acc_EX** | **Acc_RES** |
| **SQLGlot**                  | 74.19                                               | 70.97                                               | 60.32                                                | 60.32                                                | 55.81                                                   | 53.49                                                   | 53.85               | 46.15                | 29.27               | 20.73                | 73.33               | 66.67                |
| **jOOQ**                          | 70.97                                               | 70.97                                               | 39.68                                                | 39.68                                                | 62.79                                                   | 60.47                                                   | 84.62               | 53.85                | 47.56               | 35.37                | 80.0                | 53.33                |
| **Ora2Pg** | N/A                                        | N/A                                        | 33.33                                     | 33.33                                     | N/A                                            | N/A                                            | 76.92    | 46.15     | N/A        | N/A         | N/A        | N/A         |
| **SQLines**                  | 9.68                                                | 9.68                                                | 31.75                                                | 31.75                                                | 53.49                                                   | 48.84                                                   | 61.54               | 38.46                | 39.02               | 32.93                | 80.0                | 60.0                 |
| **GPT-4o**                     | 61.29                                               | 61.29                                               | 50.79                                                | 44.44                                                | 60.47                                                   | 55.81                                                   | 84.62               | 53.85                | 12.2                | 10.98                | 80.0                | 73.33                |
| **CrackSQL (Ours)**                          | **87.1**                                       | **74.19**                                      | **85.71**                                       | **79.37**                                       | **69.77**                                          | **67.44**                                          | **92.31**      | **61.54**       | **59.76**      | **42.68**       | **93.33**       | **80.0**        |


## 🖥️ Demo

- Homepage of the deployed translation service:

![Web Interface Homepage](./data/images/home.png)

- detailed translation process of specific translation pair:

![Web Interface Rewrite Detail](./data/images/detail.png)

## 🚀 Quick Start

### Method 1: Source Code Installation

#### 1. Clone Repository

```bash
git clone https://github.com/your-username/git
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

### Method 2: PyPI Package Installation

Install the PyPI package at the [official website](https://pypi.org/project/cracksql/0.0.0b0/).

![Web Interface Preview](./data/images/pypi.png)

```
pip install cracksql==0.0.0b0
```

An example running code using this PyPI package is below:

```python
import os

from cracksql.app_factory import create_app
from cracksql.translate import Translator
from cracksql.init_knowledge_base import initialize_kb


def initkb():
    possible_config_paths = [
        "./init_config.yaml"
    ]

    config_file = None
    for path in possible_config_paths:
        if os.path.exists(path):
            config_file = path
            break

    if not config_file:
        config_file = "./backend/config/init_config.yaml"

    try:
        initialize_kb(config_file)
    except Exception as e:
        import traceback
        traceback.print_exc()


def translate():
    target_db_config = {
        "host": "target database host",
        "port": "target database number",
        "user": "target database username",
        "password": "target database password",
        "db_name": "target database database name"
    }

    vector_config = {
        "src_kb_name": "source database knowledge base name",
        "tgt_kb_name": "target database knowledge base name"
    }

    llm_model_name = "llm model name"

    src_dialect = "source database"
    tgt_dialect = "target database"
    src_sql = "source SQL"

    translator = Translator(src_dialect=src_dialect, tgt_dialect=tgt_dialect,
                            src_sql=src_sql, model_name=llm_model_name,
                            tgt_db_config=target_db_config, vector_config=vector_config)

    translated_sql, model_ans_list,
    used_pieces, lift_histories = translator.local_to_global_rewrite()

    print(translated_sql)
    print(model_ans_list)
    print(used_pieces)
    print(lift_histories)


if __name__ == "__main__":
    app = create_app("PRODUCTION")
    app.config["SCHEDULER_OPEN"] = False
    with app.app_context():
        initkb()
        translate()

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

## 📋 TODO

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

