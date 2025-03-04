#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CrackSQL packaging script
Automatically copies code, fixes import paths and generates pip package
"""

import os
import sys
import shutil
import subprocess
import tempfile
import glob
from pathlib import Path

# Files and directory patterns to exclude
EXCLUDE_PATTERNS = [
    '__pycache__',
    '*.pyc',
    '.DS_Store',
    '.venv',
    '.idea',
    'instance',
    'logs',
    'local_models',
    'sources',
    '.git'
]

def setup_dir(source_dir, target_dir):
    """Create directory structure for packaging"""
    print(f"Creating package directory: {target_dir}")
    
    # Create cracksql package directory
    cracksql_dir = os.path.join(target_dir, 'cracksql')
    os.makedirs(cracksql_dir, exist_ok=True)
    
    # Create empty __init__.py file to make directory a package
    with open(os.path.join(cracksql_dir, '__init__.py'), 'w', encoding='utf-8') as f:
        f.write('"""CrackSQL - Intelligent SQL translation toolkit"""\n\n__version__ = "0.1.0"\n')

def copy_source_to_dir(source_dir, target_dir):
    """Copy source code to target directory"""
    print(f"Copying source from {source_dir} to {target_dir}/cracksql")
    
    cracksql_dir = os.path.join(target_dir, 'cracksql')
    
    # Iterate through all files and directories in backend directory
    for item in os.listdir(source_dir):
        src_path = os.path.join(source_dir, item)
        dst_path = os.path.join(cracksql_dir, item)
        
        # Skip excluded items
        if any(fnmatch(item, pattern) for pattern in EXCLUDE_PATTERNS):
            print(f"  - Skipping: {item}")
            continue
        
        if os.path.isdir(src_path):
            # Copy directory
            shutil.copytree(
                src_path, 
                dst_path,
                ignore=shutil.ignore_patterns(*EXCLUDE_PATTERNS)
            )
            print(f"  - Copied directory: {item}")
        else:
            # Copy file
            shutil.copy2(src_path, dst_path)
            print(f"  - Copied file: {item}")

def fnmatch(name, pattern):
    """Simple filename matching"""
    import fnmatch as fn
    return fn.fnmatch(name, pattern)

def copy_setup_files(target_dir):
    """Copy existing setup.py and related files to target directory"""
    print(f"Copying setup files to directory: {target_dir}")
    
    # Copy setup.py
    if os.path.exists('setup.py'):
        shutil.copy2('setup.py', os.path.join(target_dir, 'setup.py'))
        print(f"  - Copied file: setup.py")
    else:
        print(f"Warning: setup.py file not found, package may not build correctly")
    
    # Copy other related files
    for file in ['MANIFEST.in', 'README.md', 'LICENSE']:
        if os.path.exists(file):
            shutil.copy2(file, os.path.join(target_dir, file))
            print(f"  - Copied file: {file}")

def create_manifest_in(target_dir):
    """Check if MANIFEST.in exists in source directory, copy to target if exists, else raise error"""
    source_file = 'MANIFEST.in'
    target_file = os.path.join(target_dir, 'MANIFEST.in')
    
    if not os.path.exists(source_file):
        raise FileNotFoundError(f"Error: MANIFEST.in file not found, please create this file in project root before running packaging script")
    else:
        shutil.copy2(source_file, target_file)
        print(f"MANIFEST.in file copied: {source_file} -> {target_file}")

def create_readme(source_dir, target_dir):
    """Check if README.md exists in source directory, copy to target if exists, else raise error"""
    source_file = 'README.md'
    target_file = os.path.join(target_dir, 'README.md')
    
    if not os.path.exists(source_file):
        raise FileNotFoundError(f"Error: README.md file not found, please create this file in project root before running packaging script")
    else:
        shutil.copy2(source_file, target_file)
        print(f"README.md file copied: {source_file} -> {target_file}")

def create_license(target_dir):
    """Check if LICENSE exists in source directory, copy to target if exists, else raise error"""
    source_file = 'LICENSE'
    target_file = os.path.join(target_dir, 'LICENSE')
    
    if not os.path.exists(source_file):
        raise FileNotFoundError(f"Error: LICENSE file not found, please create this file in project root before running packaging script")
    else:
        shutil.copy2(source_file, target_file)
        print(f"LICENSE file copied: {source_file} -> {target_file}")

def run_modify_imports(script_path, dir_path):
    """Run import path fixing script"""
    print(f"Fixing import paths using script: {script_path}")
    
    # Run modification script, pointing to cracksql directory
    cracksql_dir = os.path.join(dir_path, 'cracksql')
    cmd = [sys.executable, script_path, cracksql_dir]
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"Warning output:\n{result.stderr}")
    except subprocess.CalledProcessError as e:
        print(f"Error fixing import paths:")
        print(e.stdout)
        print(e.stderr)
        raise

def run_unified_adapter(adapter_script, dir_path):
    """Run unified adapter script"""
    print(f"Running unified adapter script: {adapter_script}")
    
    if not os.path.isfile(adapter_script):
        print(f"Error: Adapter script not found: {adapter_script}")
        return False
    
    # Current directory
    original_dir = os.getcwd()
    
    try:
        # Switch to parent directory of target directory
        os.chdir(os.path.dirname(dir_path))
        
        # Run adapter script
        cmd = [sys.executable, os.path.join(original_dir, adapter_script), dir_path]
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(result.stdout)
        
        # Switch back to original directory
        os.chdir(original_dir)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running adapter script: {str(e)}")
        print(f"Error output: {e.stderr}")
        os.chdir(original_dir)
        return False
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        os.chdir(original_dir)
        return False

def build_package(dir_path):
    """Build Python package"""
    print("Starting package build...")
    
    # Switch to target directory
    original_dir = os.getcwd()
    os.chdir(dir_path)
    
    try:
        # Run setup.py to build package
        cmd_sdist = [sys.executable, 'setup.py', 'sdist']
        cmd_wheel = [sys.executable, 'setup.py', 'bdist_wheel']
        
        print("Building source distribution (sdist)...")
        subprocess.run(cmd_sdist, check=True)
        
        print("Building wheel package...")
        subprocess.run(cmd_wheel, check=True)
        
        # Switch back to original directory
        os.chdir(original_dir)
        
        # Create dist directory
        os.makedirs('dist', exist_ok=True)
        
        # Copy built packages to dist directory
        for item in glob.glob(os.path.join(dir_path, 'dist', '*')):
            dst = os.path.join('dist', os.path.basename(item))
            shutil.copy2(item, dst)
            print(f"Copied package file: {dst}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error building package: {str(e)}")
        os.chdir(original_dir)
        raise
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        os.chdir(original_dir)
        raise

def main():
    """Main function"""
    print("=" * 60)
    print("CrackSQL Packaging Script")
    print("=" * 60)
    
    # Check backend directory
    backend_dir = 'backend'
    if not os.path.isdir(backend_dir):
        print(f"Error: backend directory not found, ensure running script from project root")
        return 1
    
    # Check required script files
    required_scripts = [
        ('modify_imports.py', 'Import fixing script'),
        ('package_adapter_unified.py', 'Unified adapter script')
    ]
    
    for script_file, desc in required_scripts:
        if not os.path.isfile(script_file):
            print(f"Error: {desc} not found {script_file}")
            return 1
    
    # Check required configuration files
    required_files = [
        ('setup.py', 'Python package configuration file'),
        ('MANIFEST.in', 'Included files configuration'),
        ('setup.py', 'Python package configuration file'),
        ('MANIFEST.in', 'Included files configuration'),
        ('README.md', 'Project documentation file'),
        ('LICENSE', 'License file')
    ]
    
    for file_name, desc in required_files:
        if not os.path.isfile(file_name):
            print(f"Error: Cannot find {desc} {file_name}, please ensure this file exists in the project root directory")
            return 1
    
    # Use current directory as working directory
    build_dir = os.path.join(os.getcwd(), 'build_dir')
    
    # If directory exists, delete it first
    if os.path.exists(build_dir):
        print(f"Deleting existing build directory: {build_dir}")
        shutil.rmtree(build_dir)
    
    # Create build directory
    os.makedirs(build_dir, exist_ok=True)
    
    try:
        print(f"\n1. Setting up directory")
        setup_dir(backend_dir, build_dir)
        
        print(f"\n2. Copying source code")
        copy_source_to_dir(backend_dir, build_dir)
        
        print(f"\n3. Copying setup files")
        copy_setup_files(build_dir)
        
        # Check necessary files
        print(f"\n4. Checking required files")
        create_manifest_in(build_dir)
        create_readme(backend_dir, build_dir)
        create_license(build_dir)
        
        print(f"\n5. Running unified adapter")
        run_unified_adapter('package_adapter_unified.py', build_dir)
        
        print(f"\n6. Fixing import paths")
        run_modify_imports('modify_imports.py', build_dir)
        
        print(f"\n7. Building package")
        build_package(build_dir)
        
        print("\nPackage process completed successfully!")
        print(f"Generated package files are located in 'dist/' directory")
        
        # Cleanup: delete build directory
        print(f"\n8. Cleaning up: deleting build directory")
        shutil.rmtree(build_dir)
        
        return 0
    except Exception as e:
        print(f"\nError: Package process failed: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 