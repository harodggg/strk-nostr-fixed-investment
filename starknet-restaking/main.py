import os
from loguru import logger

# 获取一个已存在的环境变量
home_env = os.getenv('HH')
logger.info(f"HOME 的值为: {home_env}")
logger.error("error")

# 获取一个不存在的环境变量，并指定默认值
non_existent_env = os.getenv('HH', '这是一个默认值')
