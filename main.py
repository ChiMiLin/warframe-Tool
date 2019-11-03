import discord
from discord.ext import commands
import json
import datetime

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix='~')

@bot.event
async def on_ready():
    print('>>Bot is online!<<')

@bot.command()
async def Y0_time(ctx,arg1 = 1):
    await ctx.send('夜靈出現時間:')

    locationPoint = datetime.datetime(2019,11,3,1,00,00)
    now = datetime.datetime.now()
    now_noSec = datetime.datetime(now.year,now.month,now.day,now.hour,now.minute)

    count = 0
    #找到下一個夜靈出沒定位點
    i = 0
    while True:
        delta = datetime.timedelta(seconds = i*60)
        nexttime = now_noSec + delta
        if ((nexttime - locationPoint).seconds/60) % 150 == 0:
            await ctx.send(nexttime)
            count += 1
            if count == arg1:
                break
        i += 1

bot.run(jdata['TOKEN'])
