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
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Knowledge base initialization script')
    parser.add_argument('--config_file', type=str, default='./config/init_config.yaml', help='Configuration file path')
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
    """Check if database tables exist"""
    try:
        # Try to query tables in the database
        with app.app_context():
            # Use reflection to get all tables
            inspector = inspect(db.engine)
            
            # Check if key tables exist
            required_tables = ['knowledge_bases', 'json_contents', 'llm_models']
            existing_tables = inspector.get_table_names()
            
            logger.info(f"Existing database tables: {existing_tables}")
            
            # Check if all required tables exist
            for table in required_tables:
                if table not in existing_tables:
                    logger.warning(f"Missing required table: {table}")
                    return False
            
            return True
    except Exception as e:
        logger.error(f"Error checking database: {str(e)}")
        return False


@db_session_manager
def initialize_database(app=None):
    """Directly create database, suitable for production environment"""
    try:
        logger.info("Starting database initialization...")
        
        # Use passed app instance or create a new one (without initializing scheduler)
        if app is None:
            # Import necessary modules, avoiding circular imports
            from app_factory import create_app
            
            # Create app instance, but disable scheduler
            app = create_app("PRODUCTION")
            # Ensure scheduler won't start
            app.config["SCHEDULER_OPEN"] = False
        
        # Ensure instance directory exists
        instance_dir = './instance'
        if not os.path.exists(instance_dir):
            os.makedirs(instance_dir, exist_ok=True)
            logger.info(f"Created instance directory: {instance_dir}")
        
        # Perform database operations within app context
        with app.app_context():
            # Directly create all tables
            table_names = [table.name for table in db.metadata.sorted_tables]
            logger.info(f"Tables to be created: {table_names}")
            logger.info("Creating all database tables...")
            db.create_all()
            
            # Get database file path
            db_uri = app.config.get('SQLALCHEMY_DATABASE_URI', '')
            if db_uri.startswith('sqlite:///'):
                db_path = db_uri.replace('sqlite:///', '')
                logger.info(f"Database file path: {db_path}")
            
            logger.info("Database initialization successful")
            return True
            
    except Exception as e:
        logger.error(f"Database initialization failed: {str(e)}")
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
    """Initialize knowledge base from configuration"""
    if not kb_configs or not isinstance(kb_configs, list):
        logger.error("Invalid or empty knowledge base configuration")
        return False
    
    success_count = 0
    total_count = len(kb_configs)
    
    # Initialize all knowledge bases
    for kb_config in kb_configs:
        # Check required parameters
        if 'kb_name' not in kb_config:
            logger.error("Knowledge base configuration missing required parameter: kb_name")
            continue

        if 'db_type' not in kb_config:
            logger.error(f"Knowledge base {kb_config.get('kb_name', 'unknown')} configuration missing required parameter: db_type")
            continue

        if 'embedding_model' not in kb_config:
            logger.error(f"Knowledge base {kb_config.get('kb_name', 'unknown')} configuration missing required parameter: embedding_model")
            continue

        kb_name = kb_config['kb_name']
        db_type = kb_config['db_type']
        kb_info = kb_config.get('kb_info', '')
        embedding_model = kb_config['embedding_model']
        knowledge_files = kb_config.get('knowledge_files', [])

        # Check if embedding model exists
        if not check_embedding_model(embedding_model):
            logger.error(f"Embedding model {embedding_model} used by knowledge base {kb_name} does not exist")
            continue

        # Create knowledge base
        if not create_kb(kb_name, kb_info, db_type, embedding_model):
            logger.error(f"Failed to create knowledge base {kb_name}")
            continue

        # Import knowledge files
        if knowledge_files:
            for file_path in knowledge_files:
                if not import_knowledge_file(kb_name, file_path):
                    logger.warning(f"Failed to import knowledge file {file_path} into knowledge base {kb_name}")

        # Vectorize pending knowledge items
        if not vectorize_pending_items(kb_name):
            logger.warning(f"Failed to vectorize pending knowledge items in knowledge base {kb_name}")
        
        success_count += 1
        logger.info(f"Knowledge base {kb_name} initialization completed")
    
    logger.info(f"Knowledge base initialization completed: {success_count}/{total_count} successful")
    return success_count > 0


def initialize_kb(config_file_path):
    """Main function - execute initialization steps in fixed order"""

    if not config_file_path:
        logger.error("Configuration file path must be provided")
        sys.exit(1)

    # Create application context
    try:
        # Create application instance, but disable scheduler to avoid duplicate initialization
        app = create_app(config_name='PRODUCTION')
        app.config["SCHEDULER_OPEN"] = False
    except Exception as e:
        logger.error(f"Failed to create application context: {str(e)}")
        sys.exit(1)
    
    # Step 1: Check and initialize database
    try:
        db_exists = check_database_exists(app)
        if not db_exists:
            logger.warning("Database tables do not exist or are not initialized, automatically initializing database...")
            if not initialize_database(app):
                logger.error("Database initialization failed, exiting program")
                sys.exit(1)
            logger.info("Database initialization completed, continuing execution...")
    except Exception as e:
        logger.error(f"Error checking database: {str(e)}")
        sys.exit(1)

    # Load configuration file
    config = load_config(config_file_path)
    if not config:
        logger.error(f"Failed to load configuration file: {config_file_path}")
        sys.exit(1)

    # Step 2: Initialize embedding models
    if 'EMBEDDING_MODELS' in config:
        logger.info("Starting embedding models initialization...")
        if not init_embedding_models(config['EMBEDDING_MODELS']):
            logger.error("Embedding models initialization failed, exiting program")
            sys.exit(1)
        logger.info("Embedding models initialization completed")
    else:
        logger.warning("No embedding models configuration found in configuration file, skipping embedding models initialization")

    # Step 3: Initialize knowledge bases
    if 'KNOWLEDGE_BASES' in config:
        logger.info("Starting knowledge bases initialization...")
        if not init_knowledge_base_from_config(config['KNOWLEDGE_BASES']):
            logger.error("Knowledge bases initialization failed, exiting program")
            sys.exit(1)
        logger.info("Knowledge bases initialization completed")
    else:
        logger.warning("No knowledge bases configuration found in configuration file, skipping knowledge bases initialization")

    # Step 4: Initialize LLM models (if any)
    if 'LLM_MODELS' in config:
        logger.info("Starting LLM models initialization...")
        if not init_llm_models(config['LLM_MODELS']):
            logger.error("LLM models initialization failed, exiting program")
            sys.exit(1)
        logger.info("LLM models initialization completed")
    else:
        logger.warning("No LLM models configuration found in configuration file, skipping LLM models initialization")

    logger.info("All initialization steps completed")
    return True


if __name__ == "__main__":
    args = parse_args()
    initialize_kb(config_file_path=args.config_file)
