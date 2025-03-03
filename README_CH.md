# CrackSQL

<p align="center">
  <img src="./docs/images/logo.png" alt="CrackSQL Logo" width="200" height="auto" />
</p>

<p align="center">
  <b>一个强大的SQL方言转换工具，支持在不同SQL方言之间进行精确转换</b>
</p>

<p align="center">
  <a href="#-功能演示">演示</a> •
  <a href="#-快速开始">快速开始</a> •
  <a href="#-功能扩展">功能扩展</a> • 
  <a href="#-常见问题">常见问题</a> •  
  <a href="#-社区">社区</a> •  
  <a href="#-贡献者">贡献者</a> •  
  <a href="#-开源协议">开源协议</a>
</p>

<p align="center">
  <a href="./README.md">English</a> | <b>简体中文</b>
</p>

## ✨ 项目简介

CrackSQL是一个专注于SQL方言转换的工具，支持在不同SQL方言之间进行精确转换（如PostgreSQL到MySQL）。提供命令行、Python API和Web界面三种使用方式，满足不同场景下的需求。

## 📚 功能特性

- 🚀 **多方言支持**：支持PostgreSQL、MySQL、Oracle三种主流数据库方言的互转
- 🎯 **高精度转换**：基于三层转换架构，确保转换结果的准确性
- 🌟 **多种使用方式**：支持命令行、Python API和Web界面三种使用方式
- 🔍 **功能导向的语法处理**：将SQL语句分解为特定功能的语法元素
- 🧠 **基于模型的语法匹配**：采用创新的跨方言嵌入模型进行转换
- 🔄 **局部到全局的转换策略**：灵活处理复杂SQL转换场景

## 📊 性能展示

| 方言对 | 准确率 | 平均转换时间 |
|:-------:|:--------:|:------------:|
| PG → MySQL | 95% | 0.5s |
| MySQL → Oracle | 93% | 0.6s |
| Oracle → SQLite | 91% | 0.4s |

## 🖥️ 功能演示

<p align="center">
  <i>TODO: 添加界面预览图</i>
</p>

![Web界面预览](./docs/images/web-preview.png)

## 🚀 快速开始

### 方式一：Docker (暂不支持)

```bash
# 拉取镜像
docker pull cracksql:latest

# 运行容器
docker run -d -p 5173:5173 cracksql:latest

# 访问 http://localhost:5173 即可使用Web界面
```

### 方式二：源码安装

#### 1. 克隆仓库
```bash
git clone https://github.com/your-username/git
```

#### 2. 使用前后端应用
```bash
# 启动后端
cd CrackSQL/backend

# 安装依赖
conda create -n CrackSQL python=3.10
conda activate CrackSQL
pip install -r requirements.txt

# 初始化数据库
flask db init      # 初始化
flask db migrate   # 生成版本文件
flask db upgrade   # 同步到数据库

# 初始化知识库（可选项，不初始化也行，启动前端项目后，在前端手动执行）
# 1.需要先将config/init_config.yaml.copy重命名为config/init_config.yaml
# 2.修改config/init_config.yaml中的相关信息。如果要初始化知识库，Embedding Model是必填项
python3 init_knowledge_base.py --init_all

# 启动后台服务（后端服务的端口，也在app.py中修改，当前为30006）
python app.py

# 启动前端（需要安装nodejs，版本20.11.1+）
cd CrackSQL/webui

# 安装依赖
yarn cache clean
yarn install

# 启动开发服务器
yarn dev

# 访问 http://localhost:50212 即可使用Web界面

# 提示: 
# 如果想要修改前端端口号，可以在webui/vite.config.js中进行修改：port: 50212
# 如果后端Api的端口号改了，或者想使用服务器的IP，可修改webui/.env.serve-dev文件（该文件如果没有，可以将webui/.env.serve-dev_copy文件重命名为.env.serve-dev）中的VITE_APP_BASE_URL参数。
```

#### 3. 命令行使用（暂不支持）
```bash
# 初始化
python script/init.py

# 转换
python script/convert.py --source postgresql --target mysql "SELECT * FROM users LIMIT 10" \
  --source_db_type pg --target_db_type mysql \
  --target_db_host localhost --target_db_port 3306 \
  --target_db_user root --target_db_password 123456 \
  --output_file output.json
```

## 📎 功能扩展

### 增加新语法
<i>补充</i>

### 增加新数据库
<i>从头开始</i>

### 微调向量模型
<i>待补充</i>

## 🤔 常见问题

<i>TODO: 添加常见问题</i>

## 📋 待办事项

- Python API

## 👫 社区

欢迎扫码加入微信群！

<p align="center">
  <i>TODO: 添加微信群二维码</i>
</p>

## 📒 引用

如果您喜欢这个项目，欢迎引用我们的论文：

```
@misc{zhou2023llm4diag,
      title={D-Bot: Database Diagnosis System using Large Language Models}, 
      author={Xuanhe Zhou, Guoliang Li, Zhaoyan Sun, Zhiyuan Liu, Weize Chen, Jianming Wu, Jiesi Liu, Ruohang Feng, Guoyang Zeng},
      year={2023},
      eprint={2312.01454},
      archivePrefix={arXiv},
      primaryClass={cs.DB}
}
```

## 📧 贡献者

<a href="https://github.com/TsinghuaDatabaseGroup/DB-GPT/network/dependencies">
  <img src="https://contrib.rocks/image?repo=TsinghuaDatabaseGroup/DB-GPT" />
</a>

## 📝 开源协议

<i>TODO: 添加开源协议</i>

本项目采用 MIT 协议 - 详见 [LICENSE](LICENSE) 文件 