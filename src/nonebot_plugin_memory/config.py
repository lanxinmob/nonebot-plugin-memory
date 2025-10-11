from nonebot import get_driver, get_plugin_config
from pydantic import BaseModel, Field


class Config(BaseModel):
    memory_deepseek_api_key: str = Field(
        default="", 
        description="DeepSeek/OpenAI API 密钥，用于大模型调用。"
    )
    memory_redis_host: str = Field(
        default="localhost",
        description="Redis 服务器主机地址。"
    )
    memory_redis_port: int = Field(
        default=6379, 
        description="Redis 服务器端口。"
    )
    memory_redis_db: int = Field(
        default=0, 
        description="Redis 数据库编号。"
    )


# 配置加载
plugin_config: Config = get_plugin_config(Config)
global_config = get_driver().config

MEMORY_DEEPSEEK_API_KEY: str = plugin_config.memory_deepseek_api_key
MEMORY_REDIS_HOST: str = plugin_config.memory_redis_host
MEMORY_REDIS_PORT: int = plugin_config.memory_redis_port
MEMORY_REDIS_DB: int = plugin_config.memory_redis_db

NICKNAME: str = next(iter(global_config.nickname), "")
