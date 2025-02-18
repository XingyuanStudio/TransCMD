import sys
from os import path
from trans_core import *
from json import loads
from pyperclip import copy
from trans_core import logger


class TransCMD:
    def __init__(self):
        try:
            # 获取程序运行目录
            if getattr(sys, 'frozen', False):
                # 如果是 exe 运行
                base_path = path.dirname(sys.executable)
            else:
                # 如果是 py 文件运行
                base_path = path.dirname(path.abspath(__file__))
            
            config_path = path.join(base_path, "config.json")
            
            # 读取配置
            with open(config_path, "r", encoding="utf-8") as f:
                self.config = loads(f.read())

            logger.info("成功加载配置文件")
            self.res = self.run_trans()
            print(self.res)  # 只输出翻译结果
            copy(self.res)
            logger.info("翻译完成并已复制到剪贴板: " + self.res)

        except Exception as e:
            logger.error(f"程序运行出错: {str(e)}")
            raise

    def run_trans(self):
        try:
            text = " ".join(sys.argv[1:])
            logger.info(f"待翻译文本: {text}")
            
            if self.config["trans_type"] == "model_trans":
                logger.info("使用模型翻译")
                return model_trans(
                    text, self.config["source_lang"], self.config["target_lang"], self.config["model_trans.model_name"]
                )

            elif self.config["trans_type"] == "crewler_trans":
                logger.info("使用爬虫翻译")
                return crewler_trans(
                    text, self.config["source_lang"], self.config["target_lang"]
                )
            elif self.config["trans_type"] == "tencent_trans":
                logger.info("使用腾讯云翻译")
                return tencent_trans(
                    text, self.config["source_lang"], self.config["target_lang"], self.config["tencent_trans.secret_id"], self.config["tencent_trans.secret_key"]
                )

            else:
                logger.error(f"未知的翻译类型: {self.config['trans_type']}")
                raise ValueError(f"未知的翻译类型：{self.config['trans_type']}")

        except Exception as e:
            logger.error(f"翻译过程出错: {str(e)}")
            raise

if __name__ == "__main__":
    try:
        TransCMD()
    except Exception as e:
        logger.error(f"程序异常退出: {str(e)}")
        sys.exit(1)