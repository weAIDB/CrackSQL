#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
导入修复脚本 - 修改所有文件中的导入语句，使它们在pip安装模式下也能正常工作
"""

import os
import re
import sys
import glob
from typing import List, Dict

# 定义需要处理的文件和目录模式
FILE_PATTERNS = [
    # 核心模块文件
    'models.py',
    'app.py',
    'app_factory.py',
    'init_knowledge_base.py',
    # API模块
    'api/*.py',
    'api/services/*.py',
    'api/utils/*.py',
    # 配置模块
    'config/*.py',
    # LLM模型模块
    'llm_model/*.py',
    # 向量存储模块
    'vector_store/*.py',
    # 工具模块
    'utils/*.py',
    # 其他模块
    'retriever/*.py',
    'task/*.py',
    'translator/*.py',
    'preprocessor/*.py',
    'doc_process/*.py',
]

# 不应该被替换为cracksql.xxx的模块列表
# 包括Python标准库和常用的第三方库
DO_NOT_REPLACE_MODULES = [
    # Python标准库
    'os', 'sys', 're', 'json', 'time', 'datetime', 'logging', 'logging.config',
    'math', 'random', 'collections', 'itertools', 'functools', 'types',
    'traceback', 'copy', 'shutil', 'tempfile', 'glob', 'pathlib', 'uuid',
    'hashlib', 'base64', 'urllib', 'http', 'socket', 'email', 'smtplib',
    'threading', 'multiprocessing', 'subprocess', 'asyncio', 'concurrent',
    'unittest', 'pytest', 'yaml', 'csv', 'xml', 'html', 'argparse', 'configparser',
    'decimal', 'fractions', 'numbers', 'statistics', 'pickle', 'codecs', 'platform',
    'io', 'enum', 'string', 'calendar', 'zlib', 'gzip', 'tarfile', 'zipfile',
    'struct', 'array', 'heapq', 'bisect', 'weakref', 'abc', 'typing', 'importlib',
    # 常用第三方库
    'flask', 'flask_cors', 'flask_migrate', 'flask_sqlalchemy', 'flask_caching',
    'sqlalchemy', 'pymysql', 'requests', 'numpy', 'pandas', 'sklearn', 'torch',
    'openai', 'langchain', 'transformers', 'chromadb', 'tiktoken', 'sqlglot',
    'gunicorn', 'pytest', 'jwt', 'pyyaml', 'alembic', 'click', 'werkzeug',
    'jinja2', 'markupsafe', 'itsdangerous', 'six', 'setuptools', 'pip',
    'wheel', 'virtualenv', 'pytz', 'chardet', 'idna', 'certifi', 'urllib3',
    'tqdm', 'packaging', 'antlr4', 'flask_apscheduler', 'langchain_openai', 
    'langchain_community', 'tenacity', 'langchain_core', 'langchain_community'
]

# 导入替换规则
IMPORT_REPLACEMENTS = {
    # 从任何模块导入
    r'^from ([\w\.]+) import (.*)': 
        lambda match: process_from_import(match),
    
    # 直接导入模块
    r'^import ([\w\.]+)(.*)': 
        lambda match: process_import(match),
}

def process_from_import(match):
    """处理from xxx import yyy形式的导入"""
    module = match.group(1)
    imports = match.group(2)
    
    # 检查是否是不应该被替换的模块
    if any(module == lib or module.startswith(f"{lib}.") for lib in DO_NOT_REPLACE_MODULES):
        return f"from {module} import {imports}"
    
    # 简化导入替换逻辑，去掉存根的创建
    return f"from cracksql.{module} import {imports}"

def process_import(match):
    """处理import xxx形式的导入"""
    module = match.group(1)
    rest = match.group(2)
    
    # 检查是否是不应该被替换的模块
    if any(module == lib or module.startswith(f"{lib}.") for lib in DO_NOT_REPLACE_MODULES):
        return f"import {module}{rest}"
    
    # 创建一个有效的别名（去掉点号）
    alias = module.replace(".", "_")
    
    # 简化导入替换逻辑，去掉存根的创建
    return f"import cracksql.{module} as {alias}{rest}"

def get_files_to_process(base_dir: str, patterns: List[str]) -> List[str]:
    """根据模式获取需要处理的文件列表"""
    files = []
    for pattern in patterns:
        # 将模式转换为完整路径
        full_pattern = os.path.join(base_dir, pattern)
        # 使用glob匹配文件
        matched_files = glob.glob(full_pattern, recursive=True)
        files.extend(matched_files)
    
    # 过滤出.py文件并去重
    return sorted(list(set([f for f in files if f.endswith('.py')])))

def modify_file_imports(file_path: str) -> None:
    """修改文件中的导入语句"""
    print(f"处理文件: {file_path}")
    
    # 读取文件内容
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            # 尝试其他编码
            with open(file_path, 'r', encoding='latin-1') as f:
                content = f.read()
        except Exception as e:
            print(f"  - 无法读取文件，跳过: {str(e)}")
            return
    
    # 应用所有替换规则
    modified_content = content
    for pattern, replacement in IMPORT_REPLACEMENTS.items():
        def replace_func(match):
            if callable(replacement):
                return replacement(match)
            return replacement
        
        modified_content = re.sub(pattern, replace_func, modified_content, flags=re.MULTILINE)
    
    # 修复可能出现的双点号问题
    modified_content = modified_content.replace("cracksql..", "cracksql.")
    
    # 如果文件被修改，保存更改
    if modified_content != content:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            print(f"  - 文件已修改")
        except Exception as e:
            print(f"  - 保存文件时出错: {str(e)}")
    else:
        print(f"  - 文件未变化")

def main():
    """主函数"""
    print("开始修复导入语句...")
    
    # 检查命令行参数
    if len(sys.argv) > 1:
        base_dir = sys.argv[1]
    else:
        # 默认使用当前目录
        base_dir = '.'
    
    print(f"使用基础目录: {base_dir}")
    
    # 获取需要处理的文件
    files = get_files_to_process(base_dir, FILE_PATTERNS)
    print(f"找到 {len(files)} 个文件需要处理")
    
    # 处理每个文件
    for file_path in files:
        modify_file_imports(file_path)
    
    print("导入修复完成!")

if __name__ == "__main__":
    main() 