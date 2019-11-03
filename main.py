import discord
from discord.ext import commands
import json
import datetime

with open('../warframe-Tool-Token/setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix='~')

@bot.event
async def on_ready():
    print('>>Bot is online!<<')

@bot.command()
async def Y0_time(ctx,*args):
    if len(args) == 0:
        COUNT = 1
    elif len(args) > 1 or not args[0].isdigit():
        await ctx.send('輸入限制純數字且只允許一個參數')
        return
    elif int(args[0]) > 10:
        await ctx.send('顯示上限為10筆')
        return
    else:
        COUNT = int(args[0])
    
    await ctx.send('夜靈出現時間:')

    locationPoint = datetime.datetime(2019,11,3,1,00,00)
    now = datetime.datetime.now()
    now_noSec = datetime.datetime(now.year,now.month,now.day,now.hour,now.minute)

    nexttime = now_noSec
    count = 0
    #找到下一個夜靈出沒定位點
    for i in range(150):
        delta = datetime.timedelta(seconds = i*60)
        nexttime = now_noSec + delta
        if ((nexttime - locationPoint).seconds/60) % 150 == 0:
            await ctx.send(nexttime)
            count += 1
            break
    
    for i in range(COUNT - 1):
        delta = datetime.timedelta(seconds = 60*150)
        nexttime += delta
        await ctx.send(nexttime)

bot.run(jdata['TOKEN'])
