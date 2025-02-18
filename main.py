import sys
from os import path
from trans_core import *
from json import loads
from pyperclip import copy


class TransCMD:
    def __init__(self):
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

        self.res = self.run_trans()
        print(self.res)
        copy(self.res)

    def run_trans(self):
        text = " ".join(sys.argv[1:])
        
        if self.config["trans_type"] == "model_trans":
            return model_trans(
                text, self.config["source_lang"], self.config["target_lang"], self.config["model_trans.model_name"]
            )

        elif self.config["trans_type"] == "crewler_trans":
            return crewler_trans(
                text, self.config["source_lang"], self.config["target_lang"]
            )
        elif self.config["trans_type"] == "tencent_trans":
            return tencent_trans(
                text, self.config["source_lang"], self.config["target_lang"], self.config["tencent_trans.secret_id"], self.config["tencent_trans.secret_key"]
            )

        else:
            ...

TransCMD()