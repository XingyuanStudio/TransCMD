# TransCMD.trans_core

## 简介

TransCMD.trans_core 是 TransCMD 的翻译核心，它提供了翻译功能。

## 环境准备

trans_core 提供三种可用的翻译引擎：

- 本地大模型翻译

- 在线翻译，使用第三方API接口

- 在线翻译，使用爬虫技术

### 本地大模型翻译

假定您已经先安装了`ollama`，并下载了您想用的模型。

接口：

```python
trans_text(
    text: str, 
    model_name: str, 
    original_language: str = None, 
    target_language: str = None, 
    more_examples: list = None
) -> str
```

示例：

```python
trans_text(
    text="Hello, world!", 
    model_name="qwen2.5:1.5b", 
    target_language="拉丁语.Latin.Lingua Latina"
)
```

### 在线翻译，使用第三方API接口



### 在线翻译，使用爬虫技术

