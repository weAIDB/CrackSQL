#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Knowledge Base Initialization Script
Used to create knowledge base and import knowledge files
"""

import os
import json
import yaml
import time
import argparse
import subprocess
import sys
# Import application context
from app_factory import create_app
from config.db_config import db, db_session_manager
from models import KnowledgeBase, JSONContent, LLMModel
from api.services.knowledge import create_knowledge_base, add_kb_items
from config.logging_config import logger
from llm_model.embeddings import get_embeddings
from vector_store.chroma_store import ChromaStore
import asyncio
from sqlalchemy.exc import OperationalError, ProgrammingError
from sqlalchemy import text, inspect


def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description='知识库初始化脚本')
    parser.add_argument('--config_file', type=str, default='./config/init_config.yaml', help='配置文件路径')
    return parser.parse_args()




def load_config(config_file_path):
    """Load configuration file"""
    try:
        with open(config_file_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        return config
    except FileNotFoundError:
        logger.error(f"Configuration file does not exist: {config_file_path}")
        return None
    except yaml.YAMLError as e:
        logger.error(f"YAML format error: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Failed to load configuration file: {str(e)}")
        return None


def check_database_exists(app):
    """检查数据库表是否存在"""
    try:
        # 尝试查询数据库中的表
        with app.app_context():
            # 使用反射获取所有表
            inspector = inspect(db.engine)
            
            # 检查关键表是否存在
            required_tables = ['knowledge_bases', 'json_contents', 'llm_models']
            existing_tables = inspector.get_table_names()
            
            logger.info(f"现有数据库表: {existing_tables}")
            
            # 检查所有必需的表是否都存在
            for table in required_tables:
                if table not in existing_tables:
                    logger.warning(f"缺少必要的表: {table}")
                    return False
            
            return True
    except Exception as e:
        logger.error(f"检查数据库时出错: {str(e)}")
        return False


@db_session_manager
def initialize_database(app=None):
    """直接创建数据库，适用于生产环境"""
    try:
        logger.info("开始初始化数据库...")
        
        # 使用传入的应用实例或创建一个新的（不初始化调度器）
        if app is None:
            # 导入必要的模块，但避免循环导入
            from app_factory import create_app
            
            # 创建应用实例，但禁用调度器
            app = create_app("PRODUCTION")
            # 确保不会启动调度器
            app.config["SCHEDULER_OPEN"] = False
        
        # 确保实例文件夹存在
        instance_dir = './instance'
        if not os.path.exists(instance_dir):
            os.makedirs(instance_dir, exist_ok=True)
            logger.info(f"创建实例目录: {instance_dir}")
        
        # 在应用上下文中执行数据库操作
        with app.app_context():
            # 直接创建所有表
            table_names = [table.name for table in db.metadata.sorted_tables]
            logger.info(f"需要创建的表: {table_names}")
            logger.info("创建所有数据库表...")
            db.create_all()
            
            # 获取数据库文件路径
            db_uri = app.config.get('SQLALCHEMY_DATABASE_URI', '')
            if db_uri.startswith('sqlite:///'):
                db_path = db_uri.replace('sqlite:///', '')
                logger.info(f"数据库文件路径: {db_path}")
            
            logger.info("数据库初始化成功")
            return True
            
    except Exception as e:
        logger.error(f"数据库初始化失败: {str(e)}")
        return False


@db_session_manager
def init_llm_models(models_config):
    """Initialize LLM models"""
    if not models_config:
        logger.error("LLM model configuration not found, please check the LLM_MODELS section in the configuration file")
        return False

    success_count = 0
    total_count = len(models_config)

    for model_config in models_config:
        try:
            # Check required parameters
            if 'name' not in model_config:
                logger.error("LLM model configuration missing required parameter: name")
                continue

            if 'deployment_type' not in model_config:
                logger.error(
                    f"LLM model {model_config['name']} configuration missing required parameter: deployment_type")
                continue

            # Check if model already exists
            existing_model = db.session.query(LLMModel).filter_by(name=model_config['name']).first()
            if existing_model:
                logger.info(f"LLM model {model_config['name']} already exists")
                success_count += 1
                continue

            # Create new model
            model = LLMModel(
                name=model_config['name'],
                deployment_type=model_config['deployment_type'],
                category='llm',
                path=model_config.get('path'),
                api_base=model_config.get('api_base'),
                api_key=model_config.get('api_key'),
                temperature=model_config.get('temperature', 0.7),
                max_tokens=model_config.get('max_tokens'),
                description=model_config.get('description', ''),
                is_active=True
            )

            db.session.add(model)
            db.session.commit()
            logger.info(f"Successfully created LLM model: {model_config['name']}")
            success_count += 1

        except Exception as e:
            db.session.rollback()
            logger.error(f"Failed to create LLM model {model_config.get('name', 'unknown')}: {str(e)}")

    logger.info(f"LLM model initialization complete: Success {success_count}/{total_count}")
    return success_count > 0


@db_session_manager
def init_embedding_models(models_config):
    """Initialize Embedding models"""
    if not models_config:
        logger.error(
            "Embedding model configuration not found, please check the EMBEDDING_MODELS section in the configuration file")
        return False

    success_count = 0
    total_count = len(models_config)

    for model_config in models_config:
        try:
            # Check required parameters
            if 'name' not in model_config:
                logger.error("Embedding model configuration missing required parameter: name")
                continue

            if 'deployment_type' not in model_config:
                logger.error(
                    f"Embedding model {model_config['name']} configuration missing required parameter: deployment_type")
                continue

            if 'dimension' not in model_config:
                logger.error(
                    f"Embedding model {model_config['name']} configuration missing required parameter: dimension")
                continue

            # Check if model already exists
            existing_model = db.session.query(LLMModel).filter_by(name=model_config['name']).first()
            if existing_model:
                logger.info(f"Embedding model {model_config['name']} already exists")
                success_count += 1
                continue

            # Create new model
            model = LLMModel(
                name=model_config['name'],
                deployment_type=model_config['deployment_type'],
                category='embedding',
                path=model_config.get('path'),
                api_base=model_config.get('api_base'),
                api_key=model_config.get('api_key'),
                dimension=model_config['dimension'],
                description=model_config.get('description', ''),
                is_active=True
            )

            db.session.add(model)
            db.session.commit()
            logger.info(f"Successfully created Embedding model: {model_config['name']}")
            success_count += 1

        except Exception as e:
            db.session.rollback()
            logger.error(f"Failed to create Embedding model {model_config.get('name', 'unknown')}: {str(e)}")

    logger.info(f"Embedding model initialization complete: Success {success_count}/{total_count}")
    return success_count > 0


@db_session_manager
def check_embedding_model(model_name):
    """Check if vector model exists"""
    model = db.session.query(LLMModel).filter_by(name=model_name, category='embedding', is_active=True).first()
    if not model:
        logger.error(f"Vector model {model_name} does not exist or is not enabled, please initialize the model first")
        return False
    return True


@db_session_manager
def create_kb(kb_name, kb_info, db_type, embedding_model):
    """Create knowledge base"""
    # Check if knowledge base already exists
    kb = db.session.query(KnowledgeBase).filter_by(kb_name=kb_name).first()
    if kb:
        logger.info(f"Knowledge base {kb_name} already exists")
        return kb

    # Create knowledge base
    result = create_knowledge_base(
        kb_name=kb_name,
        kb_info=kb_info,
        embedding_model_name=embedding_model,
        db_type=db_type
    )

    if result.get('status'):
        logger.info(f"Knowledge base {kb_name} created successfully")
        return KnowledgeBase.query.filter_by(kb_name=kb_name).first()
    else:
        logger.error(f"Knowledge base creation failed: {result.get('msg', 'Unknown error')}")
        return None


@db_session_manager
def import_knowledge_file(kb_name, file_path):
    """Import knowledge file"""
    if not os.path.exists(file_path):
        logger.error(f"File does not exist: {file_path}")
        return False

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                items = json.load(f)
            except json.JSONDecodeError as e:
                logger.error(f"JSON parsing error: {str(e)}")
                return False

        if not isinstance(items, list):
            logger.error(f"JSON content must be in array format, current format: {type(items).__name__}")
            return False

        if len(items) == 0:
            logger.warning(f"No knowledge entries in file {file_path}")
            return True

        # Add knowledge entries
        result = add_kb_items(kb_name, items)

        if result.get('status'):
            logger.info(f"Successfully imported {len(items)} knowledge entries")
            return True
        else:
            logger.error(f"Import failed: {result.get('message', 'Unknown error')}")
            return False

    except Exception as e:
        logger.error(f"Failed to import knowledge file: {str(e)}")
        return False


@db_session_manager
def vectorize_pending_items(kb_name):
    """Vectorize pending knowledge entries"""
    # Get knowledge base
    kb = db.session.query(KnowledgeBase).filter_by(kb_name=kb_name).first()
    if not kb:
        logger.error(f"Knowledge base does not exist: {kb_name}")
        return False

    # Get pending entries
    pending_items = db.session.query(JSONContent).filter_by(
        knowledge_base_id=kb.id,
        status="pending"
    ).all()

    if not pending_items:
        logger.info("No pending knowledge entries")
        return True

    logger.info(f"Starting vectorization of {len(pending_items)} knowledge entries")

    # Group by content type
    items_by_type = {}
    for item in pending_items:
        if item.content_type not in items_by_type:
            items_by_type[item.content_type] = []
        items_by_type[item.content_type].append(item)

    # Create Chroma storage
    store = ChromaStore()

    # Process each type of entry
    for content_type, items in items_by_type.items():
        try:
            # Get embedding text
            texts = [item.embedding_text for item in items]

            # Generate vectors
            try:
                embeddings = asyncio.run(get_embeddings(texts, kb.embedding_model_name))
            except Exception as e:
                logger.error(f"Failed to generate vectors: {str(e)}")
                # Update failure status
                for item in items:
                    item.status = "failed"
                    item.error_msg = f"Failed to generate vectors: {str(e)}"
                db.session.commit()
                continue

            # Prepare metadata
            metadatas = []
            ids = []

            for i, item in enumerate(items):
                # Generate vector ID
                vector_id = f"{item.id}_{content_type}"

                # Update database record
                item.vector_id = vector_id
                item.status = "completed"

                # Prepare metadata
                metadata = {
                    'content_id': str(item.id),
                    'knowledge_base_id': str(kb.id),
                    'content_type': item.content_type,
                    'content': json.dumps(item.content)
                }
                metadatas.append(metadata)
                ids.append(vector_id)

            # Add to vector database
            try:
                store.add_texts(
                    kb_name=kb_name,
                    content_type=content_type,
                    texts=texts,
                    embeddings=embeddings,
                    metadatas=metadatas,
                    ids=ids
                )
            except Exception as e:
                logger.error(f"Failed to add vectors to vector database: {str(e)}")
                # Update failure status
                for item in items:
                    item.status = "failed"
                    item.error_msg = f"Failed to add vectors to vector database: {str(e)}"
                db.session.commit()
                continue

            # Commit database changes
            db.session.commit()

            logger.info(f"Successfully vectorized {len(items)} knowledge entries of type {content_type}")

        except Exception as e:
            db.session.rollback()
            logger.error(f"Failed to vectorize knowledge entries of type {content_type}: {str(e)}")

            # Update failure status
            for item in items:
                item.status = "failed"
                item.error_msg = str(e)
            db.session.commit()

            return False

    return True


def init_knowledge_base_from_config(kb_configs):
    """从配置初始化知识库"""
    if not kb_configs or not isinstance(kb_configs, list):
        logger.error("知识库配置无效或为空")
        return False
    
    success_count = 0
    total_count = len(kb_configs)
    
    # 初始化所有知识库
    for kb_config in kb_configs:
        # 检查必需参数
        if 'kb_name' not in kb_config:
            logger.error("知识库配置缺少必需参数: kb_name")
            continue

        if 'db_type' not in kb_config:
            logger.error(f"知识库 {kb_config.get('kb_name', 'unknown')} 配置缺少必需参数: db_type")
            continue

        if 'embedding_model' not in kb_config:
            logger.error(f"知识库 {kb_config.get('kb_name', 'unknown')} 配置缺少必需参数: embedding_model")
            continue

        kb_name = kb_config['kb_name']
        db_type = kb_config['db_type']
        kb_info = kb_config.get('kb_info', '')
        embedding_model = kb_config['embedding_model']
        knowledge_files = kb_config.get('knowledge_files', [])

        # 检查嵌入模型是否存在
        if not check_embedding_model(embedding_model):
            logger.error(f"知识库 {kb_name} 使用的嵌入模型 {embedding_model} 不存在")
            continue

        # 创建知识库
        if not create_kb(kb_name, kb_info, db_type, embedding_model):
            logger.error(f"创建知识库 {kb_name} 失败")
            continue

        # 导入知识文件
        if knowledge_files:
            for file_path in knowledge_files:
                if not import_knowledge_file(kb_name, file_path):
                    logger.warning(f"知识库 {kb_name} 导入知识文件 {file_path} 失败")

        # 向量化待处理的知识条目
        if not vectorize_pending_items(kb_name):
            logger.warning(f"知识库 {kb_name} 向量化待处理的知识条目失败")
        
        success_count += 1
        logger.info(f"知识库 {kb_name} 初始化完成")
    
    logger.info(f"知识库初始化完成: 成功 {success_count}/{total_count}")
    return success_count > 0


def initialize_kb(config_file_path):
    """主函数 - 按固定顺序执行初始化步骤"""

    if not config_file_path:
        logger.error("必须提供配置文件路径")
        sys.exit(1)

    # 创建应用上下文
    try:
        # 创建应用实例，但禁用调度器以避免重复初始化
        app = create_app(config_name='PRODUCTION')
        app.config["SCHEDULER_OPEN"] = False
    except Exception as e:
        logger.error(f"创建应用上下文失败: {str(e)}")
        sys.exit(1)
    
    # 步骤1: 检查并初始化数据库
    try:
        db_exists = check_database_exists(app)
        if not db_exists:
            logger.warning("数据库表不存在或未初始化，正在自动初始化数据库...")
            if not initialize_database(app):
                logger.error("数据库初始化失败，程序退出")
                sys.exit(1)
            logger.info("数据库初始化完成，继续执行...")
    except Exception as e:
        logger.error(f"检查数据库时出错: {str(e)}")
        sys.exit(1)

    # 加载配置文件
    config = load_config(config_file_path)
    if not config:
        logger.error(f"加载配置文件失败: {config_file_path}")
        sys.exit(1)

    # 步骤2: 初始化嵌入模型
    if 'EMBEDDING_MODELS' in config:
        logger.info("开始初始化嵌入模型...")
        if not init_embedding_models(config['EMBEDDING_MODELS']):
            logger.error("嵌入模型初始化失败，程序退出")
            sys.exit(1)
        logger.info("嵌入模型初始化完成")
    else:
        logger.warning("配置文件中未找到嵌入模型配置，跳过嵌入模型初始化")

    # 步骤3: 初始化知识库
    if 'KNOWLEDGE_BASES' in config:
        logger.info("开始初始化知识库...")
        if not init_knowledge_base_from_config(config['KNOWLEDGE_BASES']):
            logger.error("知识库初始化失败，程序退出")
            sys.exit(1)
        logger.info("知识库初始化完成")
    else:
        logger.warning("配置文件中未找到知识库配置，跳过知识库初始化")

    # 步骤4: 初始化LLM模型（如果有）
    if 'LLM_MODELS' in config:
        logger.info("开始初始化LLM模型...")
        if not init_llm_models(config['LLM_MODELS']):
            logger.error("LLM模型初始化失败，程序退出")
            sys.exit(1)
        logger.info("LLM模型初始化完成")
    else:
        logger.warning("配置文件中未找到LLM模型配置，跳过LLM模型初始化")

    logger.info("所有初始化步骤已完成")
    return True


if __name__ == "__main__":
    args = parse_args()
    initialize_kb(config_file_path=args.config_file)
