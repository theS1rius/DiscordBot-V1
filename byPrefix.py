import os
# 導入Discord.py模組
import discord
# 導入commands指令模組
from discord.ext import commands

from dotenv import load_dotenv


# 載入 .env 檔案
load_dotenv()

discord_token_venus = os.getenv("DISCORD_TOKEN_VENUS")

# intents是要求機器人的權限
intents = discord.Intents.all()
# command_prefix是前綴符號，可以自由選擇($, #, &...)
bot = commands.Bot(command_prefix = "%", intents = intents)

@bot.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

@bot.command()
# 輸入%Hello呼叫指令
async def Hello(ctx):
    # 回覆Hello, world!
    await ctx.send("你好呀！我是機器人。測試一下")


if __name__ == "__main__":
    bot.run(discord_token_venus)
