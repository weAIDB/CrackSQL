#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CrackSQL 打包脚本
自动复制代码、修复导入路径并生成pip包
"""

import os
import sys
import shutil
import subprocess
import tempfile
import glob
from pathlib import Path

# 需要排除的文件和目录模式
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
    """创建目录结构，准备打包"""
    print(f"创建打包目录: {target_dir}")
    
    # 创建cracksql包目录
    cracksql_dir = os.path.join(target_dir, 'cracksql')
    os.makedirs(cracksql_dir, exist_ok=True)
    
    # 创建空的__init__.py文件，使目录成为包
    with open(os.path.join(cracksql_dir, '__init__.py'), 'w', encoding='utf-8') as f:
        f.write('"""CrackSQL - 智能SQL转译工具包"""\n\n__version__ = "0.1.0"\n')

def copy_source_to_dir(source_dir, target_dir):
    """复制源代码到目标目录"""
    print(f"从 {source_dir} 复制源码到 {target_dir}/cracksql")
    
    cracksql_dir = os.path.join(target_dir, 'cracksql')
    
    # 遍历backend目录中的所有文件和目录
    for item in os.listdir(source_dir):
        src_path = os.path.join(source_dir, item)
        dst_path = os.path.join(cracksql_dir, item)
        
        # 跳过需要排除的项目
        if any(fnmatch(item, pattern) for pattern in EXCLUDE_PATTERNS):
            print(f"  - 跳过: {item}")
            continue
        
        if os.path.isdir(src_path):
            # 复制目录
            shutil.copytree(
                src_path, 
                dst_path,
                ignore=shutil.ignore_patterns(*EXCLUDE_PATTERNS)
            )
            print(f"  - 复制目录: {item}")
        else:
            # 复制文件
            shutil.copy2(src_path, dst_path)
            print(f"  - 复制文件: {item}")

def fnmatch(name, pattern):
    """简单的文件名匹配"""
    import fnmatch as fn
    return fn.fnmatch(name, pattern)

def copy_setup_files(target_dir):
    """复制已存在的setup.py和相关文件到目标目录"""
    print(f"复制setup文件到目录: {target_dir}")
    
    # 复制setup.py
    if os.path.exists('setup.py'):
        shutil.copy2('setup.py', os.path.join(target_dir, 'setup.py'))
        print(f"  - 复制文件: setup.py")
    else:
        print(f"警告: 未找到setup.py文件，包将无法正确构建")
    
    # 复制其他相关文件
    for file in ['MANIFEST.in', 'README.md', 'LICENSE']:
        if os.path.exists(file):
            shutil.copy2(file, os.path.join(target_dir, file))
            print(f"  - 复制文件: {file}")

def create_manifest_in(target_dir):
    """检查原始目录中是否存在MANIFEST.in文件，如果存在则复制到目标目录，不存在则报错"""
    source_file = 'MANIFEST.in'
    target_file = os.path.join(target_dir, 'MANIFEST.in')
    
    if not os.path.exists(source_file):
        raise FileNotFoundError(f"错误: MANIFEST.in文件不存在，请在项目根目录创建此文件后再运行打包脚本")
    else:
        shutil.copy2(source_file, target_file)
        print(f"MANIFEST.in文件已复制: {source_file} -> {target_file}")

def create_readme(source_dir, target_dir):
    """检查原始目录中是否存在README.md文件，如果存在则复制到目标目录，不存在则报错"""
    source_file = 'README.md'
    target_file = os.path.join(target_dir, 'README.md')
    
    if not os.path.exists(source_file):
        raise FileNotFoundError(f"错误: README.md文件不存在，请在项目根目录创建此文件后再运行打包脚本")
    else:
        shutil.copy2(source_file, target_file)
        print(f"README.md文件已复制: {source_file} -> {target_file}")

def create_license(target_dir):
    """检查原始目录中是否存在LICENSE文件，如果存在则复制到目标目录，不存在则报错"""
    source_file = 'LICENSE'
    target_file = os.path.join(target_dir, 'LICENSE')
    
    if not os.path.exists(source_file):
        raise FileNotFoundError(f"错误: LICENSE文件不存在，请在项目根目录创建此文件后再运行打包脚本")
    else:
        shutil.copy2(source_file, target_file)
        print(f"LICENSE文件已复制: {source_file} -> {target_file}")

def run_modify_imports(script_path, dir_path):
    """运行导入修复脚本"""
    print(f"修复导入路径，使用脚本: {script_path}")
    
    # 运行修改脚本，指向cracksql目录
    cracksql_dir = os.path.join(dir_path, 'cracksql')
    cmd = [sys.executable, script_path, cracksql_dir]
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"警告输出:\n{result.stderr}")
    except subprocess.CalledProcessError as e:
        print(f"修复导入路径时出错:")
        print(e.stdout)
        print(e.stderr)
        raise

def run_unified_adapter(adapter_script, dir_path):
    """运行统一适配器脚本"""
    print(f"运行统一适配器脚本: {adapter_script}")
    
    if not os.path.isfile(adapter_script):
        print(f"错误: 找不到适配器脚本: {adapter_script}")
        return False
    
    # 当前目录
    original_dir = os.getcwd()
    
    try:
        # 切换到目标目录的父目录
        os.chdir(os.path.dirname(dir_path))
        
        # 运行适配器脚本
        cmd = [sys.executable, os.path.join(original_dir, adapter_script), dir_path]
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(result.stdout)
        
        # 切回原目录
        os.chdir(original_dir)
        return True
    except subprocess.CalledProcessError as e:
        print(f"运行适配器脚本出错: {str(e)}")
        print(f"错误输出: {e.stderr}")
        os.chdir(original_dir)
        return False
    except Exception as e:
        print(f"发生错误: {str(e)}")
        os.chdir(original_dir)
        return False

def build_package(dir_path):
    """构建Python包"""
    print("开始构建包...")
    
    # 切换到目标目录
    original_dir = os.getcwd()
    os.chdir(dir_path)
    
    try:
        # 运行setup.py构建包
        cmd_sdist = [sys.executable, 'setup.py', 'sdist']
        cmd_wheel = [sys.executable, 'setup.py', 'bdist_wheel']
        
        print("构建源码分发包(sdist)...")
        subprocess.run(cmd_sdist, check=True)
        
        print("构建wheel包...")
        subprocess.run(cmd_wheel, check=True)
        
        # 切回原目录
        os.chdir(original_dir)
        
        # 创建dist目录
        os.makedirs('dist', exist_ok=True)
        
        # 复制构建的包到dist目录
        for item in glob.glob(os.path.join(dir_path, 'dist', '*')):
            dst = os.path.join('dist', os.path.basename(item))
            shutil.copy2(item, dst)
            print(f"复制包文件: {dst}")
        
    except subprocess.CalledProcessError as e:
        print(f"构建包时出错: {str(e)}")
        os.chdir(original_dir)
        raise
    except Exception as e:
        print(f"发生错误: {str(e)}")
        os.chdir(original_dir)
        raise

def main():
    """主函数"""
    print("=" * 60)
    print("CrackSQL 打包脚本")
    print("=" * 60)
    
    # 检查backend目录
    backend_dir = 'backend'
    if not os.path.isdir(backend_dir):
        print(f"错误: 找不到backend目录，确保在项目根目录运行此脚本")
        return 1
    
    # 检查必要的脚本文件
    required_scripts = [
        ('modify_imports.py', '导入修复脚本'),
        ('package_adapter_unified.py', '统一适配器脚本')
    ]
    
    for script_file, desc in required_scripts:
        if not os.path.isfile(script_file):
            print(f"错误: 找不到{desc} {script_file}")
            return 1
    
    # 检查必要的配置文件
    required_files = [
        ('setup.py', 'Python包配置文件'),
        ('MANIFEST.in', '包含文件配置'),
        ('README.md', '项目说明文件'),
        ('LICENSE', '许可证文件')
    ]
    
    for file_name, desc in required_files:
        if not os.path.isfile(file_name):
            print(f"错误: 找不到{desc} {file_name}，请确保此文件存在于项目根目录")
            return 1
    
    # 使用当前目录作为工作目录
    build_dir = os.path.join(os.getcwd(), 'build_dir')
    
    # 如果目录已存在，先删除
    if os.path.exists(build_dir):
        print(f"删除已存在的构建目录: {build_dir}")
        shutil.rmtree(build_dir)
    
    # 创建构建目录
    os.makedirs(build_dir, exist_ok=True)
    
    try:
        print(f"\n1. 设置目录")
        setup_dir(backend_dir, build_dir)
        
        print(f"\n2. 复制源代码")
        copy_source_to_dir(backend_dir, build_dir)
        
        print(f"\n3. 复制setup文件")
        copy_setup_files(build_dir)
        
        # 检查必要的文件
        print(f"\n4. 检查必要文件")
        create_manifest_in(build_dir)
        create_readme(backend_dir, build_dir)
        create_license(build_dir)
        
        print(f"\n5. 运行统一适配器")
        run_unified_adapter('package_adapter_unified.py', build_dir)
        
        print(f"\n6. 修复导入路径")
        run_modify_imports('modify_imports.py', build_dir)
        
        print(f"\n7. 构建包")
        build_package(build_dir)
        
        print("\n打包过程成功完成!")
        print(f"生成的包文件位于 'dist/' 目录")
        
        # 清理工作：删除构建目录
        print(f"\n8. 清理：删除构建目录")
        shutil.rmtree(build_dir)
        
        return 0
    except Exception as e:
        print(f"\n错误: 打包过程失败: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 