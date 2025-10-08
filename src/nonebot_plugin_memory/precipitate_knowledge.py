import asyncio
from datetime import datetime, timedelta
import json
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message
from nonebot.exception import FinishedException
from nonebot.log import logger
from nonebot.matcher import Matcher
from nonebot.params import ArgPlainText, CommandArg
from nonebot_plugin_apscheduler import scheduler
import redis.asyncio as redis
from .config import REDIS_HOST, REDIS_PORT, REDIS_DB 
from . import chat


@scheduler.scheduled_job("cron", hour=22, minute=0)
async def precipitate_knowledge():
    redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)
    if not redis_client:
        logger.warning("Redis 客户端未连接,跳过沉淀任务")
        return
    
    all_logs = await redis_client.lrange("all_memory", 0, -1)

    try:
        logs = []
        past_time = datetime.now() - timedelta(days=1)
        for log in all_logs:
            log = json.loads(log)
            log_time = datetime.fromisoformat(log["time"])
            if log_time >= past_time:
                logs.append(log)

            PROFILE_PREFIX = "user_profile:"

            user_id = {log["user_id"] for log in logs if log["role"] == "user"}
            for uid in user_id:
                user_log = [log for log in logs if log["role"] == "user" and log["user_id"] == uid]
                nickname = user_log[0]["nickname"]
                chat_log = [log["content"] for log in user_log]
                key = f"{PROFILE_PREFIX}{uid}"
                old_profile = await redis_client.get(key)
                if old_profile:
                    old_profile = json.loads(old_profile)
                    prompt_user = f"""
                    以下是你对用户 {nickname}({uid}) 的历史画像：
                    {old_profile}

                    以下是该用户在最近一天的发言记录：
                    {chat_log}

                    请基于历史画像 + 新的发言，更新用户画像，保持相同格式并合理融合：
                    【核心特质】
                    【行为模式】
                    【关系定位】
                    【茉子认知画像】
                    """
                else:
                    prompt_user = f"""
                    请根据用户 {nickname} ({uid}) 最近24小时的发言,  
                    从你的视角总结这个用户的画像，按照以下模板输出：
                    【核心特质】
                    【行为模式】
                    【关系定位】
                    【茉子认知画像】
                    以下是该用户在最近一天的发言记录：
                    {chat_log}
                    """
                response = await asyncio.wait_for(
                    chat.client.chat.completions.create(
                        model="deepseek-chat",
                        messages=[
                            {
                                "role": "system",
                                "content": "你是千恋万花中的常陆茉子，一个有点小恶魔性格、喜欢捉弄人但内心善良的女生",
                            },
                            {"role": "user", "content": prompt_user},
                        ],
                        temperature=0.5,
                        max_tokens=2048,
                    ),
                    timeout=30.0,
                )
                profile_text = response.choices[0].message.content.strip()
                user_profile = {
                    "user_id": uid,
                    "nickname": nickname,
                    "profile_text": profile_text,
                    "last_updated": datetime.now().isoformat(),
                }
                await redis_client.set(key, json.dumps(user_profile))
                logger.success(f"已建立 {nickname} 的茉子印象")

    except Exception as e:
        logger.error(f"调用LLM出错: {e}")
        return


memory_handler = on_command("可塑性记忆", aliases={"memory"}, priority=10, block=True)


@memory_handler.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()
    if plain_text:
        matcher.set_arg("target_id", args)


@memory_handler.got("target_id", prompt="要查看茉子对谁的印象~？")
async def handle_get_weather(target_id: str = ArgPlainText()):
    target_id = target_id.strip()

    redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
    if not redis_client:
        await memory_handler.finish("Redis 连接未配置，无法查询记忆。")
        return

    key = f"user_profile:{target_id}"
    try:
        profile_json = redis_client.get(key)
        if profile_json:
            profile_data = json.loads(profile_json)
            memory_text = profile_data.get("profile_text", "记忆数据中缺少画像文本。")
            nickname = profile_data.get("nickname")
            await memory_handler.finish(f"对{nickname}({target_id})的茉子印象:\n\n{memory_text}")
        else:
            await memory_handler.finish(f"茉子暂时没有对用户 {target_id} 的记忆。")

    except FinishedException:
        await memory_handler.finish("这份记忆报告，茉子已经整理完毕啦！请查收~ ૮₍ ˶•⤙•˶ ₎ა")
    except Exception as e:
        logger.error(f"查询 Redis 失败: {e}")
