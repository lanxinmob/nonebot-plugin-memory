from nonebot import get_driver, get_plugin_config
from pydantic import BaseModel, Field


class Config(BaseModel):
    deepseek_api_key: str = Field(
        default="", 
        alias="DEEPSEEK_API_KEY", 
        description="DeepSeek/OpenAI API 密钥，用于大模型调用。"
    )
    redis_host: str = Field(
        default="localhost", 
        alias="REDIS_HOST",
        description="Redis 服务器主机地址。"
    )
    redis_port: int = Field(
        default=6379, 
        alias="REDIS_PORT",
        description="Redis 服务器端口。"
    )
    redis_db: int = Field(
        default=0, 
        alias="REDIS_DB",
        description="Redis 数据库编号。"
    )


# 配置加载
plugin_config: Config = get_plugin_config(Config)
global_config = get_driver().config

DEEPSEEK_API_KEY: str = plugin_config.deepseek_api_key
REDIS_HOST: str = plugin_config.redis_host
REDIS_PORT: int = plugin_config.redis_port
REDIS_DB: int = plugin_config.redis_db

NICKNAME: str = next(iter(global_config.nickname), "")
