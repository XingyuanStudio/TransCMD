# TransCMD

TransCMD 是轻便易用的一个命令行翻译工具，支持多种翻译方式，包括本地模型翻译和在线翻译服务。

## 功能特点

1. 多种翻译引擎支持：
   - 本地大语言模型翻译
   - 腾讯云翻译服务
   - 爬虫翻译（开发中）

2. 便捷的命令行操作：
   - 直接翻译命令行参数
   - 自动复制翻译结果到剪贴板

3. 智能语言检测：
   - 自动识别源语言
   - 中英互译模式

4. 完善的日志系统：
   - 详细的运行日志
   - 错误追踪支持

## 快速开始

1. 安装依赖：

    pip install -r requirements.txt

2. 配置翻译服务：

编辑 config.json：

    {
        "trans_type": "tencent_trans",  # 或 "model_trans"
        "source_lang": "auto",
        "target_lang": "auto",
        
        "model_trans.model_name": "Qwen2.5:1.5b",
        "tencent_trans.secret_id": "您的SecretId",
        "tencent_trans.secret_key": "您的SecretKey"
    }

3. 使用示例：

    tc Hello, world!
    你好，世界！

    tc 苹果
    Apple

## 安装说明

### 从源码安装

    git clone https://github.com/XingyuanStudio/TransCMD.git
    cd TransCMD
    pip install -r requirements.txt

### 使用发行版

1. 从 Releases 下载最新版本
2. 解压到任意目录
3. 将程序目录添加到系统 PATH

## 环境要求

- Python 3.8 或更高版本
- 如果使用本地模型翻译：
  - Ollama 服务
  - 足够的系统内存（建议 8GB 以上）
- 如果使用腾讯云翻译：
  - 有效的腾讯云账号
  - API 密钥配置

## 项目结构

    TransCMD/
    ├── trans_core/           # 翻译核心
    │   ├── offline_model_trans.py    # 本地模型翻译
    │   ├── online_tencent_trans.py   # 腾讯云翻译
    │   └── online_crewler_trans.py   # 爬虫翻译（开发中）
    ├── config.json          # 配置文件
    ├── main.py             # 主程序
    └── README.md           # 说明文档

## 常见问题

1. 找不到配置文件：
   - 确保 config.json 与程序源文件或可执行文件在同一目录
   - 检查文件权限

2. 翻译服务报错：
   - 检查网络连接
   - 验证 API 密钥配置
   - 查看日志文件获取详细信息

## 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建您的特性分支
3. 提交您的更改
4. 确保代码风格符合规范
5. 提交 Pull Request

## 许可证

本项目采用 MPL v2.0 许可证 - 详见 [LICENSE](LICENSE.md) 文件

## 作者

- Xingyuan Studio
- 邮箱：dus0963@outlook.com
- 项目地址：https://github.com/XingyuanStudio/TransCMD 