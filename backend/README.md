# CrackSQL

CrackSQL是一个强大的SQL转换和优化工具，支持多种数据库类型之间的SQL语句转换。

## 安装

```bash
pip install cracksql
```

## 使用方法

### 作为Python包使用

```python
from cracksql import init_app, init_db, DatabaseConfig, DatabaseType

# 初始化应用
app = init_app(config_name='DEVELOPMENT')

# 初始化数据库
init_db(app)

# 创建数据库配置
db_config = DatabaseConfig(
    host='localhost',
    port=3306,
    database='test',
    username='root',
    password='password',
    db_type=DatabaseType.MYSQL,
    description='Test database'
)

# 使用应用上下文
with app.app_context():
    # 添加配置到数据库
    from cracksql import db
    db.session.add(db_config)
    db.session.commit()
```

### 作为Web服务运行

1. 设置配置文件 `config/config.yaml`
2. 运行服务器：

```bash
# 使用 Flask 开发服务器
python app.py

# 或使用 Gunicorn
gunicorn wsgi_gunicorn:app
```

## 配置

配置文件位于 `config/config.yaml`，主要配置项包括：

- 数据库连接信息
- 日志配置
- API设置
- 其他自定义配置

## API文档

### 数据库配置

- `DatabaseConfig`: 数据库配置模型
- `DatabaseType`: 数据库类型枚举（MySQL、PostgreSQL、Oracle）

### 重写历史

- `RewriteHistory`: SQL重写历史记录
- `RewriteStatus`: 重写状态枚举
- `RewriteProcess`: 重写过程记录

### 知识库

- `KnowledgeBase`: 知识库模型
- `JSONContent`: JSON内容存储
- `LLMModel`: LLM模型配置

## 开发

1. 克隆仓库
2. 安装依赖：`pip install -r requirements.txt`
3. 运行测试：`python -m pytest tests/`

## 许可证

MIT License 