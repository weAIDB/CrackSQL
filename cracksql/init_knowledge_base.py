#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Knowledge Base Initialization Script
Used to create knowledge base and import knowledge files
"""

import os
import sys
import json
import time
import yaml
import argparse
import subprocess

# Import application context
import asyncio
from sqlalchemy.exc import OperationalError, ProgrammingError
from sqlalchemy import text

from cracksql.app_factory import create_app
from cracksql.models import KnowledgeBase, JSONContent, LLMModel
from cracksql.api.services.knowledge import create_knowledge_base, add_kb_items
from cracksql.config.db_config import db
from cracksql.config.logging_config import logger
from cracksql.llm_model.embeddings import get_embeddings
from cracksql.vector_store.chroma_store import ChromaStore

# Create application context
app = create_app(config_name="PRODUCTION")


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


def check_database_exists():
    """Check if database exists and initialize"""
    try:
        # Try to query the database, using text() function to wrap SQL statement
        db.session.execute(text("SELECT * from knowledge_bases limit 1;"))
        return True
    except (OperationalError, ProgrammingError) as e:
        error_msg = str(e).lower()
        if "does not exist" in error_msg or "no such table" in error_msg or "unknown database" in error_msg:
            logger.warning("Database or table does not exist, initialization required")
            return False
        else:
            logger.error(f"Database connection error: {str(e)}")
            raise
    except Exception as e:
        logger.error(f"Error checking database: {str(e)}")
        raise


def initialize_database():
    """Initialize database"""
    try:
        logger.info("Starting database initialization...")

        # Execute Flask-Migrate commands
        commands = [
            ["flask", "db", "init"],
            ["flask", "db", "migrate", "-m", "Initial migration"],
            ["flask", "db", "upgrade"]
        ]

        for cmd in commands:
            logger.info(f"Executing command: {' '.join(cmd)}")
            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.returncode != 0:
                logger.error(f"Command execution failed: {' '.join(cmd)}")
                logger.error(f"Error message: {result.stderr}")
                return False

            logger.info(f"Command output: {result.stdout}")

        logger.info("Database initialization successful")
        return True

    except Exception as e:
        logger.error(f"Database initialization failed: {str(e)}")
        return False


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
            existing_model = LLMModel.query.filter_by(name=model_config['name']).first()
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


def init_embedding_models(models_config):
    """Initialize Embedding models"""
    if not models_config:
        logger.error("Embedding model configuration not found, please check the "
                     "EMBEDDING_MODELS section in the configuration file")
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
            existing_model = LLMModel.query.filter_by(name=model_config['name']).first()
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


def check_embedding_model(model_name):
    """Check if vector model exists"""
    model = LLMModel.query.filter_by(name=model_name, category='embedding', is_active=True).first()
    if not model:
        logger.error(f"Vector model {model_name} does not exist or is not enabled, please initialize the model first")
        return False
    return True


def create_kb(kb_name, kb_info, db_type, embedding_model):
    """Create knowledge base"""
    # Check if knowledge base already exists
    kb = KnowledgeBase.query.filter_by(kb_name=kb_name).first()
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


def vectorize_pending_items(kb_name):
    """Vectorize pending knowledge entries"""
    # Get knowledge base
    kb = KnowledgeBase.query.filter_by(kb_name=kb_name).first()
    if not kb:
        logger.error(f"Knowledge base does not exist: {kb_name}")
        return False

    # Get pending entries
    pending_items = JSONContent.query.filter_by(
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


def init_knowledge_base_from_config(kb_config):
    """Initialize knowledge base from configuration"""
    # Check required parameters
    if 'kb_name' not in kb_config:
        logger.error("Knowledge base configuration missing required parameter: kb_name")
        return False

    if 'db_type' not in kb_config:
        logger.error(
            f"Knowledge base {kb_config.get('kb_name', 'unknown')} configuration missing required parameter: db_type")
        return False

    if 'embedding_model' not in kb_config:
        logger.error(
            f"Knowledge base {kb_config.get('kb_name', 'unknown')} configuration missing required parameter: embedding_model")
        return False

    kb_name = kb_config['kb_name']
    db_type = kb_config['db_type']
    kb_info = kb_config.get('kb_info', '')
    embedding_model = kb_config['embedding_model']
    knowledge_files = kb_config.get('knowledge_files', [])

    # Check vector model
    if not check_embedding_model(embedding_model):
        logger.error(f"Failed to initialize knowledge base {kb_name}: Vector model does not exist")
        return False

    # Create knowledge base
    kb = create_kb(
        kb_name=kb_name,
        kb_info=kb_info,
        db_type=db_type,
        embedding_model=embedding_model
    )

    if not kb:
        return False

    # Import knowledge files
    success = True
    files_processed = 0

    for file_path in knowledge_files:
        if os.path.exists(file_path):
            logger.info(f"Starting import of knowledge file: {file_path}")
            if import_knowledge_file(kb_name, file_path):
                files_processed += 1
            else:
                success = False
        else:
            logger.warning(f"Knowledge file does not exist: {file_path}")

    if files_processed == 0 and knowledge_files:
        logger.warning(f"Knowledge base {kb_name} did not successfully import any knowledge files")

    # Vectorize pending knowledge entries
    if not vectorize_pending_items(kb_name):
        success = False

    if success:
        logger.info(f"Knowledge base {kb_name} initialization complete")
    else:
        logger.warning(f"Knowledge base {kb_name} initialization partially complete, some operations failed")

    return success


def initialize_cracksql(config_file, init_all=False,
                        init_llm=False, init_embedding=False, init_kb=False):
    """Main function"""
    # Check if database exists
    try:
        db_exists = check_database_exists()
        if db_exists and not init_all and not init_llm:
            logger.info("Database already exists, skipping database initialization")
            return
        if not db_exists:
            logger.warning("Database does not exist or is not initialized, automatically initializing database...")
            if not initialize_database():
                logger.error("Database initialization failed, exiting program")
                sys.exit(1)
            # Wait for database initialization to complete
            logger.info("Waiting for database initialization to complete...")
            time.sleep(2)
            logger.info("Database initialization complete, continuing execution...")
    except Exception as e:
        logger.error(f"Error checking database: {str(e)}")
        sys.exit(1)

    # Load configuration file
    config = load_config(config_file)
    if not config:
        logger.error(f"Failed to load configuration file: {config_file}")
        sys.exit(1)

    # Initialize LLM models
    if init_all or init_llm:
        if not init_llm_models(config.get('LLM_MODELS', [])):
            logger.error("Failed to initialize LLM models")
            if init_llm:  # If only initializing LLM models, exit on failure
                sys.exit(1)

    # Initialize Embedding models
    if init_all or init_embedding:
        if not init_embedding_models(config.get('EMBEDDING_MODELS', [])):
            logger.error("Failed to initialize Embedding models")
            if init_embedding:  # If only initializing Embedding models, exit on failure
                sys.exit(1)

    # Initialize all knowledge bases
    if init_all or init_kb:
        kb_configs = config.get('KNOWLEDGE_BASES', [])
        if not kb_configs:
            logger.warning("No knowledge base configuration found in configuration file")
            sys.exit(0)

        success_count = 0
        total_count = len(kb_configs)

        # Initialize all knowledge bases
        for kb_config in kb_configs:
            if init_knowledge_base_from_config(kb_config):
                success_count += 1

        logger.info(f"Knowledge base initialization complete: Success {success_count}/{total_count}")
        sys.exit(0 if success_count > 0 else 1)

    # If only initializing models, exit after completion
    if init_llm or init_embedding:
        sys.exit(0)

    # If no operation specified, display help information
    if not (init_all or init_llm or init_embedding or init_kb):
        logger.error("Please specify an operation to perform, such as "
                     "`--init_all, --init_llm, --init_embedding, --init_kb`, etc.")
        parser = argparse.ArgumentParser(description='Knowledge Base Initialization Script')
        parser.print_help()
        sys.exit(1)
