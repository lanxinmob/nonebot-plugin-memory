<div align="center">
    <a href="https://v2.nonebot.dev/store">
    <img src="https://raw.githubusercontent.com/fllesser/nonebot-plugin-template/refs/heads/resource/.docs/NoneBotPlugin.svg" width="310" alt="logo"></a>

## 可塑性记忆
## ✨ nonebot-plugin-memory ✨
[![LICENSE](https://img.shields.io/github/license/lanxinmob/nonebot-plugin-memory.svg)](./LICENSE)
[![pypi](https://img.shields.io/pypi/v/nonebot-plugin-memory.svg)](https://pypi.python.org/pypi/nonebot-plugin-memory)
[![python](https://img.shields.io/badge/python-3.10|3.11|3.12|3.13-blue.svg)](https://www.python.org)
[![uv](https://img.shields.io/badge/package%20manager-uv-black?style=flat-square&logo=uv)](https://github.com/astral-sh/uv)
<br/>
[![ruff](https://img.shields.io/badge/code%20style-ruff-black?style=flat-square&logo=ruff)](https://github.com/astral-sh/ruff)
[![pre-commit](https://results.pre-commit.ci/badge/github/lanxinmob/nonebot-plugin-memory/master.svg)](https://results.pre-commit.ci/latest/github/lanxinmob/nonebot-plugin-memory/master)

</div>

## 📖 介绍
为每位用户生成独立画像的记忆插件。对跟bot对话的每个人形成记忆，生成有趣的用户档案，用于下次生成回复，也可以通过指令查看已有的用户档案。

## 功能
- 自动保存用户发言
- 每日生成或更新用户画像
- 指令查看印象


## 💿 安装

```bash
pip install nonebot-plugin-memory
```

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-memory --upgrade
使用 **pypi** 源安装

    nb plugin install nonebot-plugin-memory --upgrade -i "https://pypi.org/simple"
使用**清华源**安装

    nb plugin install nonebot-plugin-memory --upgrade -i "https://pypi.tuna.tsinghua.edu.cn/simple"

</details>

## 💾 持久化存储 

本插件依赖 Redis 数据库来实现用户档案和聊天记忆的持久化存储，需自行安装和启动 Redis 服务。

使用 Docker (推荐)

```Bash
# 仅供本机插件连接；数据保存在 Docker volume 中
docker run --name nonebot-redis -p 127.0.0.1:6379:6379 -v nonebot-redis-data:/data -d redis:7 redis-server --appendonly yes
```
在 Linux 上安装 (以 Ubuntu/Debian 为例)
```Bash
# 安装 Redis 服务器
sudo apt update
sudo apt install redis-server

# 检查服务状态
sudo systemctl status redis-server
#确保服务状态显示为 active (running)，插件即可通过默认配置（localhost:6379）连接。
```

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项  | 必填  | 默认值 |   说明   |
| :-----: | :---: | :----: | :------: |
| memory_deepseek_api_key  |  是   |   无   | DeepSeek API 密钥，插件需要此密钥来驱动大模型的对话和画像生成功能 |
|memory_redis_host| 	否	|localhost|	Redis 数据库服务器的主机地址。 |
|memory_redis_port|	否	|6379|	Redis 数据库服务器的端口。 |
|memory_redis_db	|否	|0	|Redis 数据库编号。|
- 如果将 Redis 运行在非默认地址或端口，需要在 `.env` 文件中配置 `memory_redis_host` 和 `memory_redis_port` 来覆盖插件代码中的默认值


## 🎉 使用
### 指令表
| 指令  | 权限  | 需要@ | 范围  |   说明   |
| :---: | :---: | :---: | :---: | :------: |
| /可塑性记忆 | 所有  |  需要   | 所有  | 输入用户id查看档案 |

### 提示词
- 系统提示词 `SYSTEM_PROMPT` 设定为千恋万花中的常陆茉子，可以自行更换为其他设定。
