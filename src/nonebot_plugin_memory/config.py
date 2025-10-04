from nonebot import get_driver, get_plugin_config
from pydantic import BaseModel, Field


class Config(BaseModel):
    DEEPSEEK_API_KEY: str = Field(
        default="", alias="DEEPSEEK_API_KEY", description="DeepSeek/OpenAI API 密钥，用于大模型调用。"
    )


# 配置加载
plugin_config: Config = get_plugin_config(Config)
global_config = get_driver().config

DEEPSEEK_API_KEY: str = plugin_config.DEEPSEEK_API_KEY
# 全局名称
NICKNAME: str = next(iter(global_config.nickname), "")
