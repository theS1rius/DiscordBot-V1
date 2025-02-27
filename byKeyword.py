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
    if message.author == client.user:
        return
    
    responses = {
        "你好": "你好呀！我是機器人。",
        "做什麼": "我可以回覆你的訊息。",
        "怎麼做": "我依照關鍵字回答訊息。",
        "你叫什麼名字": "我是你的聊天機器人！",
        "天氣如何": "我目前無法查看天氣喔！",
        "你幾歲了": "我是虛擬的，沒有年齡！",
        "你喜歡什麼": "我喜歡和你聊天！",
        "今天天氣": "你可以查看天氣預報網站哦！",
        "再見": "再見！希望很快再見到你！",
        "講個笑話": "好的，這是個冷笑話……",
        "吃飯了嗎": "我不需要吃飯，但你要記得吃喔！",
        "你在哪裡": "我在這裡陪你聊天呀！",
        "現在幾點": "我不會看時間，但你可以看看時鐘喔！",
        "推薦電影": "最近有很多好看的電影喔，你可以試試 IMDb！",
        "你會唱歌嗎": "我不會唱歌，但我可以給你推薦音樂！",
        "怎麼學習 Python": "你可以看看 Python 官方文件或一些線上課程！",
        "有什麼好玩的": "你可以玩遊戲、看電影或學點新東西！",
        "你會講故事嗎": "當然！從前有一個……",
        "我好無聊": "你可以試著學習新東西或找朋友聊天！",
        "推薦一本書": "我建議你試試《哈利波特》或其他熱門書籍！"
    }

    # 如果使用者輸入 "幫助" 或 "指令列表"，回傳所有關鍵字
    if message.content in ["幫助", "指令列表"]:
        keyword_list = "\n".join(responses.keys())  # 把關鍵字組成列表
        await message.channel.send(f"📌 我支援的關鍵字有：\n```\n{keyword_list}\n```\n請輸入其中一個關鍵字來與我互動！")
    
    response = responses.get(message.content, None)
    if response:
        await message.channel.send(response)

client.run("token")