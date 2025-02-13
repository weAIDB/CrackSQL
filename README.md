# 👋 CrackSQL 是一个强大的SQL方言转换工具，支持在不同SQL方言之间进行精确转换(如PostgreSQL到MySQL)。提供命令行、Python API和Web界面三种使用方式。

# 数据库 PG → MySQL

<p align="center">
  <a href="#-demo">演示</a> •
  <a href="#-quickstart">快速开始</a> •
  <a href="#-doc2knowledge">知识与工具</a> • 
  <a href="#-FAQ">常见问题</a> •  
  <a href="#-community">社区</a> •  
  <a href="#-contributors">贡献者</a> •  
  <a href="#-license">开源协议</a> •  
</p>

[English](./README_EN.md) | 简体中文

## 📚 功能特性

- 🚀 **多方言支持**: 支持PostgreSQL、MySQL、Oracle三种主流数据库方言的互转
- 🎯 **高精度转换**: 基于三层转换架构，确保转换结果的准确性
- 🌟 **多种使用方式**: 支持命令行和Web界面三种使用方式

- **功能导向的语法处理**: 将SQL语句分解为特定功能的语法元素
- **基于模型的语法匹配**: 采用创新的跨方言嵌入模型进行转换
- **局部到全局的转换策略**: 灵活处理复杂SQL转换场景

## 📊 性能展示

等待时间提示

| 方言对 | 准确率 | 平均转换时间 |
|-------|--------|------------|
| PG → MySQL | 95% | 0.5s |
| MySQL → Oracle | 93% | 0.6s |
| Oracle → SQLite | 91% | 0.4s |


<span id="-demo"></span>
## 🖥️ 功能演示

TODO: 添加界面预览图
![Web界面预览](./docs/images/web-preview.png)


<span id="-quickstart"></span>
## 🚀 快速开始

### 方式一：Docker

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
# 
git clone https://github.com/your-username/git
```


#### 2. 可使用带前后端的应用
```bash
# 启动后端
cd CrackSQL/backend
# 安装依赖
conda create -n CrackSQL python=3.10
conda activate CrackSQL
pip install -r requirements.txt

# 初始化数据库
flask db init  初始化
flask db migrate  生成版本文件
flask db upgrade  同步到数据库

# 可以启动后台服务
python app.py

# 启动前端（需要安装nodejs，版本18.15.0+）
# 进入前端目录
cd CrackSQL/webui
# 安装依赖
npm install
# 启动开发服务器
npm run dev
访问 http://localhost:5003 即可使用Web界面
```

#### 3. 命令行使用
```bash
# 初始化
python script/init.py
# 转换
python script/convert.py --source postgresql --target mysql "SELECT * FROM users LIMIT 10" --source_db_type pg --target_db_type mysql --target_db_host localhost --target_db_port 3306 --target_db_user root --target_db_password 123456 --output_file output.json
```



<span id="-doc2knowledge"></span>
## 📎 功能扩展
### 增加新语法
补充

### 增加新数据库
从头开始

### 微调向量模型

<span id="-FAQ"></span>
## 🤔 常见问题
TODO: 添加常见问题

## TODO
- Python API

<span id="-community"></span>
👫 欢迎扫码加入微信群！


## 📒 引用
论文
Feel free to cite us (paper link) if you like this project.
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

<span id="-contributors"></span>
## 📧 贡献者
<a href="https://github.com/TsinghuaDatabaseGroup/DB-GPT/network/dependencies">
  <img src="https://contrib.rocks/image?repo=TsinghuaDatabaseGroup/DB-GPT" />
</a>


<span id="-license"></span>
## 📝 开源协议
TODO: 添加开源协议
本项目采用 MIT 协议 - 详见 [LICENSE](LICENSE) 文件

