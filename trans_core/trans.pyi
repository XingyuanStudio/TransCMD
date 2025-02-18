from typing import Optional

def model_trans(
    text: str,
    source_lang: str = 'auto',
    target_lang: str = 'auto',
    model_name: str = 'Qwen2.5:1.5b'
) -> Optional[str]: ...

def tencent_trans(
    text: str,
    source_lang: str = 'auto',
    target_lang: str = 'auto',
    secret_id: Optional[str] = None,
    secret_key: Optional[str] = None
) -> Optional[str]: ... 