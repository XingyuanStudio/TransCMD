from tencentcloud.common import credential
from tencentcloud.tmt.v20180321 import tmt_client, models
import ollama
import json
from typing import Optional, Dict, Any

class Translator:
    def __init__(self, tencent_config: Optional[Dict[str, str]] = None):
        """
        初始化翻译器
        Args:
            tencent_config: 腾讯云配置，包含 secret_id 和 secret_key
        """
        self.tencent_client = None
        if tencent_config:
            cred = credential.Credential(tencent_config["secret_id"], tencent_config["secret_key"])
            self.tencent_client = tmt_client.TmtClient(cred, "ap-beijing")

    def translate(self, 
                 text: str, 
                 source_lang: str = 'auto', 
                 target_lang: str = 'zh', 
                 use_api: bool = True,
                 model_name: str = None,
                 **kwargs) -> Optional[str]:
        """
        统一的翻译接口
        Args:
            text: 要翻译的文本
            source_lang: 源语言，默认auto自动识别
            target_lang: 目标语言，默认zh中文
            use_api: 是否使用在线API，默认True
            model_name: 使用离线模型时的模型名称
            **kwargs: 其他参数
        Returns:
            str: 翻译后的文本，失败返回None
        """
        try:
            if use_api:
                return self._tencent_trans(text, source_lang, target_lang)
            else:
                return self._model_trans(text, model_name, source_lang, target_lang, **kwargs)
        except Exception as e:
            print(f"翻译失败：{str(e)}")
            return None

    def _tencent_trans(self, text: str, source_lang: str, target_lang: str) -> str:
        """腾讯云翻译实现"""
        if not self.tencent_client:
            raise ValueError("未配置腾讯云凭证")

        # 创建请求对象
        req = models.TextTranslateRequest()
        
        # 设置请求参数
        req.SourceText = text
        req.Source = source_lang
        req.Target = target_lang
        req.ProjectId = 0

        # 发送请求
        resp = self.tencent_client.TextTranslate(req)
        return resp.TargetText

    def _model_trans(self, text: str, model_name: str, 
                    source_lang: str, target_lang: str, **kwargs) -> str:
        """离线模型翻译实现"""
        if not model_name:
            raise ValueError("未指定模型名称")

        system_message = f"""你是一个严格的翻译工具。你的唯一任务是进行文本翻译：
1. 把用户的文字从 {source_lang} 翻译成 {target_lang}
2. 如果语言是'auto', 那么请检测语言并：若用户输入的是中文，请翻译成英文，反之请翻译成中文
3. 永远只输出翻译后的文字，不要输出任何其他内容"""

        response = ollama.chat(
            model=model_name,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": text}
            ]
        )
        return response.message.content

def test_translation():
    """测试翻译功能"""
    # 配置示例
    config = {
        "secret_id": "您的SecretId",
        "secret_key": "您的SecretKey"
    }
    
    # 创建翻译器实例
    translator = Translator(config)
    
    # 测试用例
    test_cases = [
        ("Hello, world!", "en", "zh", True),
        ("你好，世界！", "auto", "en", True),
        ("Python programming", "en", "zh", False, "Qwen2.5:1.5b"),
    ]
    
    for case in test_cases:
        text = case[0]
        kwargs = {
            "source_lang": case[1],
            "target_lang": case[2],
            "use_api": case[3],
        }
        if len(case) > 4:
            kwargs["model_name"] = case[4]
            
        print(f"\n原文：{text}")
        result = translator.translate(text, **kwargs)
        print(f"译文：{result}")
        print(f"使用{'API' if case[3] else '模型'}翻译")

if __name__ == "__main__":
    test_translation() 