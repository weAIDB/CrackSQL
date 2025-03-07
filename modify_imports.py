#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Import Fix Script - Modify import statements in all files to work correctly in pip install mode
"""

import os
import re
import sys
import glob
from typing import List, Dict

# List of files and directory patterns to process
FILE_PATTERNS = [
    # Core module files
    'models.py',
    'app.py',
    'app_factory.py',
    'init_knowledge_base.py',
    # API modules
    'api/*.py',
    'api/services/*.py',
    'api/utils/*.py',
    # Configuration modules
    'config/*.py',
    # LLM model modules
    'llm_model/*.py',
    # Vector storage modules
    'vector_store/*.py',
    # Utility modules
    'utils/*.py',
    # Other modules
    'retriever/*.py',
    'task/*.py',
    'translator/*.py',
    'preprocessor/*.py',
    'preprocessor/*/*.py',
    'preprocessor/*/*/*.py',
    'doc_process/*.py',
    'translate.py',
    'cracksql.py',
]

# List of modules that should not be replaced with cracksql.xxx
# Includes Python standard libraries and common third-party libraries
DO_NOT_REPLACE_MODULES = [
    # Python standard libraries
    'os', 'sys', 're', 'json', 'time', 'datetime', 'logging', 'logging.config',
    'math', 'random', 'collections', 'itertools', 'functools', 'types',
    'traceback', 'copy', 'shutil', 'tempfile', 'glob', 'pathlib', 'uuid',
    'hashlib', 'base64', 'urllib', 'http', 'socket', 'email', 'smtplib',
    'threading', 'multiprocessing', 'subprocess', 'asyncio', 'concurrent',
    'unittest', 'pytest', 'yaml', 'csv', 'xml', 'html', 'argparse', 'configparser',
    'decimal', 'fractions', 'numbers', 'statistics', 'pickle', 'codecs', 'platform',
    'io', 'enum', 'string', 'calendar', 'zlib', 'gzip', 'tarfile', 'zipfile',
    'struct', 'array', 'heapq', 'bisect', 'weakref', 'abc', 'typing', 'importlib',
    # Common third-party libraries
    'flask', 'flask_cors', 'flask_migrate', 'flask_sqlalchemy', 'flask_caching',
    'sqlalchemy', 'pymysql', 'requests', 'numpy', 'pandas', 'sklearn', 'torch',
    'openai', 'langchain', 'transformers', 'chromadb', 'tiktoken', 'sqlglot',
    'gunicorn', 'pytest', 'jwt', 'pyyaml', 'alembic', 'click', 'werkzeug',
    'jinja2', 'markupsafe', 'itsdangerous', 'six', 'setuptools', 'pip',
    'wheel', 'virtualenv', 'pytz', 'chardet', 'idna', 'certifi', 'urllib3',
    'tqdm', 'packaging', 'antlr4', 'flask_apscheduler', 'langchain_openai', 
    'langchain_community', 'tenacity', 'langchain_core', 'langchain_community', 
    'psycopg2', 'sqlalchemy', 'cx_Oracle', 'paramiko', 'func_timeout', 'oracledb'
]

# Import replacement rules
IMPORT_REPLACEMENTS = {
    # Import from any module
    r'^from ([\w\.]+) import (.*)': 
        lambda match: process_from_import(match),
    
    # Direct import of module
    r'^import ([\w\.]+)(.*)': 
        lambda match: process_import(match),
}

def process_from_import(match):
    """Process from xxx import yyy style imports"""
    module = match.group(1)
    imports = match.group(2)
    
    # Check if it's a module that should not be replaced
    if any(module == lib or module.startswith(f"{lib}.") for lib in DO_NOT_REPLACE_MODULES):
        return f"from {module} import {imports}"
    
    # Simplified import replacement logic, remove the creation of a stub
    return f"from cracksql.{module} import {imports}"

def process_import(match):
    """Process import xxx style imports"""
    module = match.group(1)
    rest = match.group(2)
    
    # Check if it's a module that should not be replaced
    if any(module == lib or module.startswith(f"{lib}.") for lib in DO_NOT_REPLACE_MODULES):
        return f"import {module}{rest}"
    
    # Create a valid alias (remove dot)
    alias = module.replace(".", "_")
    
    # Simplified import replacement logic, remove the creation of a stub
    return f"import cracksql.{module} as {alias}{rest}"

def get_files_to_process(base_dir: str, patterns: List[str]) -> List[str]:
    """Get the list of files to process based on patterns"""
    files = []
    for pattern in patterns:
        # Convert pattern to full path
        full_pattern = os.path.join(base_dir, pattern)
        # Use glob to match files
        matched_files = glob.glob(full_pattern, recursive=True)
        files.extend(matched_files)
    
    # Filter out .py files and remove duplicates
    return sorted(list(set([f for f in files if f.endswith('.py')])))

def modify_file_imports(file_path: str) -> None:
    """Modify import statements in the file"""
    print(f"Processing file: {file_path}")
    
    # Read file content
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            # Try other encoding
            with open(file_path, 'r', encoding='latin-1') as f:
                content = f.read()
        except Exception as e:
            print(f"  - Unable to read file, skipping: {str(e)}")
            return
    
    # Apply all replacement rules
    modified_content = content
    for pattern, replacement in IMPORT_REPLACEMENTS.items():
        def replace_func(match):
            if callable(replacement):
                return replacement(match)
            return replacement
        
        modified_content = re.sub(pattern, replace_func, modified_content, flags=re.MULTILINE)
    
    # Fix potential double dot issues
    modified_content = modified_content.replace("cracksql..", "cracksql.")
    
    # If the file was modified, save changes
    if modified_content != content:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            print(f"  - File modified")
        except Exception as e:
            print(f"  - Error saving file: {str(e)}")
    else:
        print(f"  - File unchanged")

def main():
    """Main function"""
    print("Starting import statement fix...")
    
    # Check command line arguments
    if len(sys.argv) > 1:
        base_dir = sys.argv[1]
    else:
        # Default to current directory
        base_dir = '.'
    
    print(f"Using base directory: {base_dir}")
    
    # Get files to process
    files = get_files_to_process(base_dir, FILE_PATTERNS)
    print(f"Found {len(files)} files to process")
    
    # Process each file
    for file_path in files:
        modify_file_imports(file_path)
    
    print("Import fix completed!")

if __name__ == "__main__":
    main() 