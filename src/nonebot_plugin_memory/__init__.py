from nonebot import  require
from nonebot.plugin import PluginMetadata

require("nonebot_plugin_apscheduler")
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="nonebot-plugin-memory",
    description="对跟bot对话的每个人形成记忆，生成有趣用户档案，用于下次生成回复",
    usage="https://github.com/lanxinmob/nonebot-plugin-memory/blob/master/README.md",
    type="application",
    homepage="https://github.com/lanxinmob/nonebot-plugin-memory",
    config=Config,
    supported_adapters={"~onebot.v11"},
)

from . import chat, precipitate_knowledge  # noqa: F401
