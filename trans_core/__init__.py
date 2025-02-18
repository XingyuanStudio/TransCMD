from .offline_model_trans import model_trans
from .online_crewler_trans import crewler_trans
from .online_tencent_trans import tencent_trans
import logging
from logging.handlers import RotatingFileHandler
import os

__all__ = ["model_trans", "crewler_trans", "tencent_trans"]

__author__ = "Xingyuan Studio"
__email__ = "dus0963@outlook.com"
__url__ = "https://github.com/XingyuanStudio/TransCMD/tree/main/trans_core"

# 配置日志
def setup_logger(name: str, log_dir: str = "logs") -> logging.Logger:
    """设置日志记录器"""
    # 创建日志目录
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # 文件处理器
    file_handler = RotatingFileHandler(
        os.path.join(log_dir, f"{name}.log"),
        maxBytes=1024*1024,  # 1MB
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setLevel(logging.INFO)
    
    # 格式化器
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)
    
    # 添加处理器
    logger.addHandler(file_handler)
    
    return logger

# 创建日志记录器
logger = setup_logger('transcmd')

