# 導入Discord.py模組
import discord

# client是跟discord連接，intents是要求機器人的權限
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

# 調用event函式庫
@client.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份 --> {client.user}")

@client.event
# 當頻道有新訊息
async def on_message(message):
    # 排除機器人本身的訊息，避免無限循環
    if message.author == client.user:
        return
    # 新訊息包含Hello，回覆Hello, world!
    if message.content == "Hello":
        await message.channel.send("你好呀！我是機器人。")
    if message.content == "做什麼":
        await message.channel.send("我可以回覆你的訊息。")
    if message.content == "怎麼做":
        await message.channel.send("我依照關鍵字'Hello'、'做什麼'、'怎麼做'回答訊息。")

client.run("token")
