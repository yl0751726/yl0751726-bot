import discord
from discord.ext import commands
import json
import random
from core.classes import Cog_Extension
#開啟setting.json並用json.load開啟 將開啟的檔案設為jdata
with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    #成員加入提示
   @commands.Cog.listener()
   async def on_memer_join(self,member):
        channel = self.bot.get_channel(int(jdata['join']))
        await channel.send(f'阿呦~這麼好喔 {member} 加入了~!')
    #成員離開提示
   @commands.Cog.listener()
   async def on_memer_leave(self,member):
        channel = self.bot.get_channel(int(jdata['LEAVE']))
        await channel.send(f'阿呦~ {member} 離開了~真是太遜了!')
    #特定詞彙回覆
   @commands.Cog.listener()
   async def on_message(self,msg):
        if '應該' in msg.content and msg.author != self.bot.user:
            await msg.channel.send(jdata['應該'])

        if '該不會' in msg.content and msg.author != self.bot.user:
            await msg.channel.send(jdata['該不會'])

        

def setup(bot):
    bot.add_cog(Event(bot))