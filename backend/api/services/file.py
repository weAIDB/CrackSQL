import os
import time
from typing import Tuple, Dict, Any  # 引入额外的类型注解支持
from config.logging_config import logger
from flask import current_app

def save_uploaded_file_to_local(file) -> Tuple[str, str]:
    """
    将文件保存到本地
    :param file: 文件
    :return: (path: 文件地址, name: 文件名称)
    """
    # 生成一个唯一的文件名，避免文件覆盖

    # 使用时间戳和原文件名生成新的文件名
    file_name = os.path.splitext(file.filename)[0] + '_' + str(int(time.time())) + os.path.splitext(file.filename)[1]
    os.makedirs(current_app.config['UPLOAD_FOLDER'], exist_ok=True)  # 确保目录存在
    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], file_name)
    try:
        with open(file_path, 'wb') as f:
            f.write(file.read())
        logger.info(f"File saved to: {file_path}")
    except IOError as e:
        logger.error(f"Failed to save file {file_name} due to I/O error: {e}")
        raise
    return file_path, file_name


def process_uploaded_file(file) -> Dict[str, Any]:
    try:
        _, name = save_uploaded_file_to_local(file)
        logger.info(f"File {name} uploaded successfully.")
        return {"status": True, "file_name": name}
    except Exception as error:
        logger.error(f"Upload file error: {error}")
        return {"status": False, "file_name": ''}

