from typing import Optional
import logging

from .offline_model_trans import model_trans
from .online_tencent_trans import tencent_trans
from .online_crewler_trans import crewler_trans

def setup_logger(name: str, log_dir: str = "logs") -> logging.Logger:
    """
    设置日志记录器
    
    Args:
        name: 日志记录器名称
        log_dir: 日志文件目录
    
    Returns:
        logging.Logger: 配置好的日志记录器
    """
    ...

logger: logging.Logger

__all__ = ["model_trans", "tencent_trans", "crewler_trans", "logger"]

__author__: str
__email__: str
__url__: str 