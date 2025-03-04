#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CrackSQL Unified Adapter Script - Simplified Version
This script is used to modify files in the CrackSQL package to make it suitable for Python package distribution
Main features:
1. Modify app.py to make it a simple package entry point
2. Modify router.py files to avoid route registration errors
3. Modify app_factory.py to remove route registration related code
"""

import os
import sys
import re
import glob
from pathlib import Path

def modify_app_py(cracksql_dir):
    """
    Modify app.py file to make it a simple package entry point
    """
    app_py_path = os.path.join(cracksql_dir, 'app.py')
    if not os.path.exists(app_py_path):
        print(f"Warning: Cannot find app.py file: {app_py_path}")
        return False
    
    # New app.py content - simple package entry point
    new_content = '''#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CrackSQL Package Entry Point
This file serves as the entry point for the CrackSQL package, allowing users to directly import all classes and methods
"""

__version__ = "0.1.0"

# Import warnings
import warnings

# Try to import all main modules, but don't require them to exist
try:
    from . import config
except ImportError as e:
    warnings.warn(f"Failed to import config module: {str(e)}")

try:
    from . import models
except ImportError as e:
    warnings.warn(f"Failed to import models module: {str(e)}")

try:
    from . import api
except ImportError as e:
    warnings.warn(f"Failed to import api module: {str(e)}")

try:
    from . import llm_model
except ImportError as e:
    warnings.warn(f"Failed to import llm_model module: {str(e)}")

try:
    from . import vector_store
except ImportError as e:
    warnings.warn(f"Failed to import vector_store module: {str(e)}")

try:
    from . import utils
except ImportError as e:
    warnings.warn(f"Failed to import utils module: {str(e)}")

try:
    from . import retriever
except ImportError as e:
    warnings.warn(f"Failed to import retriever module: {str(e)}")

try:
    from . import task
except ImportError as e:
    warnings.warn(f"Failed to import task module: {str(e)}")

try:
    from . import translator
except ImportError as e:
    warnings.warn(f"Failed to import translator module: {str(e)}")

try:
    from . import preprocessor
except ImportError as e:
    warnings.warn(f"Failed to import preprocessor module: {str(e)}")

try:
    from . import doc_process
except ImportError as e:
    warnings.warn(f"Failed to import doc_process module: {str(e)}")

# Allow users to directly import everything from the package
'''
    
    # Write new content
    with open(app_py_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Modified app.py file to make it a simple package entry point")
    return True

def modify_app_factory_py(cracksql_dir):
    """
    Modify app_factory.py file to remove route registration related code
    """
    app_factory_py_path = os.path.join(cracksql_dir, 'app_factory.py')
    if not os.path.exists(app_factory_py_path):
        print(f"Warning: Cannot find app_factory.py file: {app_factory_py_path}")
        return False
    
    # Read original content
    with open(app_factory_py_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove router import code
    content = re.sub(r'from api\.router import router\s*', '', content)
    
    # Remove route registration code
    content = re.sub(r'register_api\(app, router\)\s*', '', content)
    
    # Write modified content
    with open(app_factory_py_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Modified app_factory.py file, removed route registration related code")
    return True

def fix_router_py(cracksql_dir):
    """
    Modify router.py files to avoid route registration errors
    """
    # Find all router.py files
    router_files = []
    for root, dirs, files in os.walk(cracksql_dir):
        for file in files:
            if file == 'router.py' or file.endswith('_router.py'):
                router_files.append(os.path.join(root, file))
    
    if not router_files:
        print("No router.py files found, skipping modification")
        return True
    
    success = True
    for router_file in router_files:
        print(f"Modifying router file: {router_file}")
        
        # Read original content
        with open(router_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Modify content, add try-except block
        new_content = '''#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Router Module - Simplified Version
This is a simplified version of router that doesn't register any routes
"""

try:
    from flask import Blueprint
except ImportError:
    # If Flask cannot be imported, create a dummy Blueprint class
    class Blueprint:
        def __init__(self, name, import_name, **kwargs):
            self.name = name
            self.import_name = import_name
        
        def route(self, rule, **options):
            def decorator(f):
                return f
            return decorator

# Create blueprint but don't register any routes
bp = Blueprint('dummy', __name__)

# Empty function that does nothing
def register_routes():
    """This function doesn't register any routes"""
    pass
'''
        
        # Write new content
        with open(router_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Modified router file: {router_file}")
    
    return success

def process_package(temp_dir):
    """
    Process package directory and modify necessary files
    """
    cracksql_dir = os.path.join(temp_dir, 'cracksql')
    if not os.path.isdir(cracksql_dir):
        print(f"Error: Cannot find cracksql directory: {cracksql_dir}")
        return False
    
    # Modify app.py
    if not modify_app_py(cracksql_dir):
        print("Warning: Failed to modify app.py")
    
    # Modify app_factory.py
    if not modify_app_factory_py(cracksql_dir):
        print("Warning: Failed to modify app_factory.py")
    
    # Modify router.py files
    if not fix_router_py(cracksql_dir):
        print("Warning: Failed to modify router.py files")
    
    return True

def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Usage: python package_adapter_unified.py <temp_directory>")
        return 1
    
    temp_dir = sys.argv[1]
    if not os.path.isdir(temp_dir):
        print(f"Error: Specified temp directory does not exist: {temp_dir}")
        return 1
    
    print("=" * 60)
    print("CrackSQL Unified Adapter Script - Simplified Version")
    print("=" * 60)
    
    if process_package(temp_dir):
        print("\nAdaptation process completed successfully!")
        return 0
    else:
        print("\nError: Adaptation process failed")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 