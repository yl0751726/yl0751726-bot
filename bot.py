import discord
from discord.ext import commands
import json
import random
import os
#開啟setting.json並用json.load開啟 將開啟的檔案設為jdata
with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)
#機器人指令前餟
bot = commands.Bot(command_prefix='[')
#機器人準備完成提示
@bot.event
async def on_ready():
    print("準備完成")
#讀取檔案,第二行為確認導入文件是否為.py文件,第三行為省略.py副檔名
for filename in os.listdir('./cmds.'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')
#確認須執行模組與執行模組是否相同,下行為啟動機器人
if __name__=="__main__":
    bot.run(jdata['TOKEN'])