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

## ✨ Project Introduction

CrackSQL is a tool focused on SQL dialect conversion, supporting precise conversion between different SQL dialects (such as PostgreSQL to MySQL). It provides three usage methods: command line, Python API, and Web interface, meeting the needs of different scenarios.

## 📚 Features

- 🚀 **Multi-dialect Support**: Supports conversion between three mainstream database dialects: PostgreSQL, MySQL, and Oracle
- 🎯 **High-precision Conversion**: Based on a three-layer conversion architecture to ensure the accuracy of conversion results
- 🌟 **Multiple Usage Methods**: Supports command line, Python API, and Web interface
- 🔍 **Function-oriented Syntax Processing**: Breaks down SQL statements into syntax elements for specific functions
- 🧠 **Model-based Syntax Matching**: Uses innovative cross-dialect embedding models for conversion
- 🔄 **Local to Global Conversion Strategy**: Flexibly handles complex SQL conversion scenarios

## 📊 Performance

| Dialect Pair | Accuracy | Average Conversion Time |
|:-------:|:--------:|:------------:|
| PG → MySQL | 95% | 0.5s |
| MySQL → Oracle | 93% | 0.6s |
| Oracle → SQLite | 91% | 0.4s |

## 🖥️ Demo

<p align="center">
  <i>TODO: Add interface preview image</i>
</p>

![Web Interface Preview](./docs/images/web-preview.png)

## 🚀 Quick Start

### Method 1: Docker (Not supported yet)

```bash
# Pull image
docker pull cracksql:latest

# Run container
docker run -d -p 5173:5173 cracksql:latest

# Visit http://localhost:5173 to use the Web interface
```

### Method 2: Source Code Installation

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
# If the backend API port number has been changed, or you want to use the server's IP, you can modify the VITE_APP_BASE_URL parameter in webui/.env.serve-dev file.
```

#### 3. Command Line Usage (Not supported yet)
```bash
# Initialize
python script/init.py

# Convert
python script/convert.py --source postgresql --target mysql "SELECT * FROM users LIMIT 10" \
  --source_db_type pg --target_db_type mysql \
  --target_db_host localhost --target_db_port 3306 \
  --target_db_user root --target_db_password 123456 \
  --output_file output.json
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

