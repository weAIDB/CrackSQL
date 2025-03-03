# CrackSQL

CrackSQL 是一个基于LLM的SQL重写工具，可以帮助用户将一种数据库的SQL语句转换为另一种数据库的SQL语句。

## 功能特点

- 支持MySQL、PostgreSQL、Oracle等多种数据库
- 使用LLM模型进行SQL转换
- 支持知识库管理
- 支持历史记录查询

## 安装方法

### 使用pip安装（推荐）

```bash
pip install cracksql
```

### 从源码安装

```bash
git clone https://github.com/your-username/cracksql.git
cd cracksql
pip install -e .
```

## 使用方法

```python
from cracksql import create_app

# 初始化应用
app = create_app('DEVELOPMENT')

# 使用SQL重写功能
from cracksql.task.sql_rewrite import SQLRewriteTask

# 创建重写任务
task = SQLRewriteTask(
    source_db_type='mysql',
    target_db_type='postgresql',
    original_sql='SELECT * FROM users WHERE id > 100'
)

# 执行重写
result = task.execute()
print(result.rewritten_sql)

# 使用知识库
from cracksql.retriever.knowledge_base import KnowledgeBase

# 初始化知识库
kb = KnowledgeBase(kb_name='mysql_to_pg')

# 添加知识
kb.add_knowledge(content={
    'type': 'function',
    'name': 'DATE_FORMAT',
    'source_syntax': 'DATE_FORMAT(date,format)',
    'target_syntax': 'TO_CHAR(date, format)'
})

# 查询知识
results = kb.search('DATE_FORMAT function equivalent in PostgreSQL')
```

## 配置说明

配置文件位于 `config/config.yaml`，主要包含以下配置项：

- 数据库连接信息
- LLM模型配置
- 日志配置
- 缓存配置

## API文档

API文档请参考 [API文档](docs/api.md)

## 许可证

MIT License 