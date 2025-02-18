# TransCMD 翻译核心

## 功能介绍

TransCMD.trans_core 提供多种翻译实现方式的核心库。

### 1. 离线模型翻译

使用本地大语言模型进行翻译，支持自动语言检测。

基本用法：

    from trans_core import model_trans
    
    # 简单翻译
    result = model_trans("Hello, world!")

高级用法：

    # 指定语言和模型
    result = model_trans(
        text="Hello, world!",
        source_lang="en",
        target_lang="zh",
        model_name="Qwen2.5:1.5b"
    )

### 2. 腾讯云翻译

使用腾讯云机器翻译服务，需要配置 API 密钥。

示例用法：

    from trans_core import tencent_trans
    
    result = tencent_trans(
        text="你好，世界！",
        source_lang="zh",
        target_lang="en",
        secret_id="您的SecretId",
        secret_key="您的SecretKey"
    )

### 3. 配置文件

配置文件 config.json 示例：

    {
        "trans_type": "tencent_trans",
        "source_lang": "auto",
        "target_lang": "auto",
        
        "model_trans.model_name": "Qwen2.5:1.5b",
        "tencent_trans.secret_id": "",
        "tencent_trans.secret_key": ""
    }

### 4. 日志系统

日志文件位于 logs 目录下，记录格式：

    2024-03-21 10:30:45 - transcmd - INFO - 成功加载配置文件
    2024-03-21 10:30:46 - transcmd - INFO - 待翻译文本: Hello, world!
    2024-03-21 10:30:47 - transcmd - INFO - 翻译完成并已复制到剪贴板

## 环境要求

1. Python 3.8 或更高版本
2. 依赖包：
   - tencentcloud-sdk-python
   - ollama
   - pyperclip

## 安装方法

使用 pip 安装依赖：

    pip install -r requirements.txt

## 异常处理

所有翻译函数在失败时都会：
1. 返回 None
2. 记录详细错误信息到日志
3. 抛出相应异常

## 作者信息

- 作者：Xingyuan Studio
- 邮箱：dus0963@outlook.com
- 项目地址：https://github.com/XingyuanStudio/TransCMD
