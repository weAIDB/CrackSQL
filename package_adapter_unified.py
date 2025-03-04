#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CrackSQL 统一适配器脚本 - 简化版
此脚本用于修改CrackSQL包中的文件，使其适合作为Python包分发
主要功能：
1. 修改app.py，使其成为简单的包入口点
2. 修改router.py文件，避免路由注册错误
3. 修改app_factory.py，删除路由注册相关代码
"""

import os
import sys
import re
import glob
from pathlib import Path

def modify_app_py(cracksql_dir):
    """
    修改app.py文件，使其成为简单的包入口点
    """
    app_py_path = os.path.join(cracksql_dir, 'app.py')
    if not os.path.exists(app_py_path):
        print(f"警告: 找不到app.py文件: {app_py_path}")
        return False
    
    # 新的app.py内容 - 简单的包入口点
    new_content = '''#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CrackSQL 包入口点
此文件作为CrackSQL包的入口点，允许用户直接导入所有类和方法
"""

__version__ = "0.1.0"

# 导入警告
import warnings

# 尝试导入所有主要模块，但不强制要求它们存在
try:
    from . import config
except ImportError as e:
    warnings.warn(f"导入config模块失败: {str(e)}")

try:
    from . import models
except ImportError as e:
    warnings.warn(f"导入models模块失败: {str(e)}")

try:
    from . import api
except ImportError as e:
    warnings.warn(f"导入api模块失败: {str(e)}")

try:
    from . import llm_model
except ImportError as e:
    warnings.warn(f"导入llm_model模块失败: {str(e)}")

try:
    from . import vector_store
except ImportError as e:
    warnings.warn(f"导入vector_store模块失败: {str(e)}")

try:
    from . import utils
except ImportError as e:
    warnings.warn(f"导入utils模块失败: {str(e)}")

try:
    from . import retriever
except ImportError as e:
    warnings.warn(f"导入retriever模块失败: {str(e)}")

try:
    from . import task
except ImportError as e:
    warnings.warn(f"导入task模块失败: {str(e)}")

try:
    from . import translator
except ImportError as e:
    warnings.warn(f"导入translator模块失败: {str(e)}")

try:
    from . import preprocessor
except ImportError as e:
    warnings.warn(f"导入preprocessor模块失败: {str(e)}")

try:
    from . import doc_process
except ImportError as e:
    warnings.warn(f"导入doc_process模块失败: {str(e)}")

# 允许用户直接从包中导入所有内容
'''
    
    # 写入新内容
    with open(app_py_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"已修改app.py文件，使其成为简单的包入口点")
    return True

def modify_app_factory_py(cracksql_dir):
    """
    修改app_factory.py文件，删除路由注册相关代码
    """
    app_factory_py_path = os.path.join(cracksql_dir, 'app_factory.py')
    if not os.path.exists(app_factory_py_path):
        print(f"警告: 找不到app_factory.py文件: {app_factory_py_path}")
        return False
    
    # 读取原始内容
    with open(app_factory_py_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 删除导入router的代码
    content = re.sub(r'from api\.router import router\s*', '', content)
    
    # 删除注册路由的代码
    content = re.sub(r'register_api\(app, router\)\s*', '', content)
    
    # 写入修改后的内容
    with open(app_factory_py_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"已修改app_factory.py文件，删除了路由注册相关代码")
    return True

def fix_router_py(cracksql_dir):
    """
    修改router.py文件，避免路由注册错误
    """
    # 查找所有router.py文件
    router_files = []
    for root, dirs, files in os.walk(cracksql_dir):
        for file in files:
            if file == 'router.py' or file.endswith('_router.py'):
                router_files.append(os.path.join(root, file))
    
    if not router_files:
        print("未找到router.py文件，跳过修改")
        return True
    
    success = True
    for router_file in router_files:
        print(f"修改router文件: {router_file}")
        
        # 读取原始内容
        with open(router_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 修改内容，添加try-except块
        new_content = '''#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Router模块 - 简化版
此文件为简化版router，不注册任何路由
"""

try:
    from flask import Blueprint
except ImportError:
    # 如果无法导入Flask，创建一个虚拟的Blueprint类
    class Blueprint:
        def __init__(self, name, import_name, **kwargs):
            self.name = name
            self.import_name = import_name
        
        def route(self, rule, **options):
            def decorator(f):
                return f
            return decorator

# 创建蓝图但不注册任何路由
bp = Blueprint('dummy', __name__)

# 空函数，不执行任何操作
def register_routes():
    """此函数不注册任何路由"""
    pass
'''
        
        # 写入新内容
        with open(router_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"已修改router文件: {router_file}")
    
    return success

def process_package(temp_dir):
    """
    处理包目录，修改必要的文件
    """
    cracksql_dir = os.path.join(temp_dir, 'cracksql')
    if not os.path.isdir(cracksql_dir):
        print(f"错误: 找不到cracksql目录: {cracksql_dir}")
        return False
    
    # 修改app.py
    if not modify_app_py(cracksql_dir):
        print("警告: 修改app.py失败")
    
    # 修改app_factory.py
    if not modify_app_factory_py(cracksql_dir):
        print("警告: 修改app_factory.py失败")
    
    # 修改router.py文件
    if not fix_router_py(cracksql_dir):
        print("警告: 修改router.py文件失败")
    
    return True

def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("用法: python package_adapter_unified.py <临时目录>")
        return 1
    
    temp_dir = sys.argv[1]
    if not os.path.isdir(temp_dir):
        print(f"错误: 指定的临时目录不存在: {temp_dir}")
        return 1
    
    print("=" * 60)
    print("CrackSQL 统一适配器脚本 - 简化版")
    print("=" * 60)
    
    if process_package(temp_dir):
        print("\n适配过程成功完成!")
        return 0
    else:
        print("\n错误: 适配过程失败")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 