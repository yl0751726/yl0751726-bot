import discord
from discord.ext import commands
import json
import random
from core.classes import Cog_Extension
#開啟setting.json並用json.load開啟 將開啟的檔案設為jdata
with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Reacrt(Cog_Extension):

    @commands.command()
    async def 圖(self,ctx):
        random_pic = random.choice(jdata['pic'])
        await ctx.send(random_pic)

    

def setup(bot):
    bot.add_cog(Reacrt(bot))