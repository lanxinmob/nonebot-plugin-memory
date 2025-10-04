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


## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项  | 必填  | 默认值 |   说明   |
| :-----: | :---: | :----: | :------: |
| DEEPSEEK_API_KEY  |  是   |   无   | 配置说明 |

## 🎉 使用
### 指令表
| 指令  | 权限  | 需要@ | 范围  |   说明   |
| :---: | :---: | :---: | :---: | :------: |
| /可塑性记忆 | 所有  |  需要   | 所有  | 输入用户id查看档案 |

