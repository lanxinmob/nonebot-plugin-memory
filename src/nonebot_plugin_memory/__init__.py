from nonebot import logger, require
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_plugin_uninfo")
require("nonebot_plugin_alconna")
require("nonebot_plugin_localstore")
require("nonebot_plugin_apscheduler")
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="nonebot-plugin-memory",
    description="对跟bot对话的每个人形成记忆，生成有趣用户档案，用于下次生成回复",
    usage="https://github.com/lanxinmob/nonebot-plugin-memory/blob/master/README.md",
    type="application",  
    homepage="https://github.com/lanxinmob/nonebot-plugin-memory",
    config=Config,
    supported_adapters=inherit_supported_adapters("nonebot_plugin_alconna", "nonebot_plugin_uninfo"),
)

from arclet.alconna import Alconna, Args, Arparma, Option, Subcommand
from nonebot_plugin_alconna import on_alconna
from nonebot_plugin_alconna.uniseg import UniMessage

pip = on_alconna(
    Alconna(
        "pip",
        Subcommand(
            "install",
            Args["package", str],
            Option("-r|--requirement", Args["file", str]),
            Option("-i|--index-url", Args["url", str]),
        ),
    )
)


@pip.handle()
async def _(result: Arparma):
    package: str = result.other_args["package"]
    logger.info(f"installing {package}")
    await UniMessage.text(package).send()

from . import chat
from . import precipitate_knowledge