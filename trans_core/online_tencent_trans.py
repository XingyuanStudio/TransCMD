from tencentcloud.common import credential
from tencentcloud.tmt.v20180321 import tmt_client, models
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

def tencent_trans(text: str, source_lang: str = 'auto', target_lang: str = 'auto', secret_id: str = None, secret_key: str = None, region: str = 'ap-beijing') -> str:
    # 初始化连接
    cred = credential.Credential(secret_id, secret_key)
    
    # 自动检测目标语言：中英互译
    if target_lang == 'auto' and source_lang == 'auto':
        # 检测语言请求
        source_lang_req = models.LanguageDetectRequest()
        source_lang_req.Text = text
        source_lang_req.ProjectId = 0
        # 检测语言
        if client.LanguageDetect(source_lang_req).Lang == 'zh':
            target_lang = 'en'
        else:
            target_lang = 'zh'

    # 翻译请求
    req = models.TextTranslateRequest()
    req.SourceText = text
    req.Source = source_lang
    req.Target = target_lang
    req.ProjectId = 0
    
    # 翻译
    client = tmt_client.TmtClient(cred, region)
    resp = client.TextTranslate(req)
    return resp.TargetText

if __name__ == "__main__":
    print(tencent_trans(
        text="Hello, world！",
        # source_lang="en",
        # target_lang="zh",
        
        region="ap-beijing"
    ))
