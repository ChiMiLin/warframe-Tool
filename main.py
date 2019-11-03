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
async def num(ctx,arg1):
    for i in range(int(arg1)):
        await ctx.send(i)

@bot.command()
async def Y0_time(ctx,*args):
    if len(args) == 0:
        COUNT = 1
    elif len(args) > 1 or not args[0].isdigit():
        await ctx.send('輸入限制純阿拉伯數字且只允許一個參數')
        return
    elif int(args[0]) > 10:
        await ctx.send('顯示上限為10筆')
        return
    else:
        COUNT = int(args[0])
    timeStr = ''
    locationPoint = datetime.datetime(2019,11,3,1,00,00)
    now = datetime.datetime.now()
    now_noSec = datetime.datetime(now.year,now.month,now.day,now.hour,now.minute)

    timeList = []
    nexttime = now_noSec
    count = 0
    #找到下一個夜靈出沒定位點
    for i in range(150):
        nexttime = now_noSec + datetime.timedelta(minutes = i)
        delta = nexttime - locationPoint
        if (delta.seconds/60 + delta.days*24*60) % 150 == 0:
            timeList.append(nexttime)
            count += 1
            break

    nexttimeDelta = (nexttime - now_noSec).seconds/60   #距離下次夜靈出現時間
    if nexttimeDelta > 100:
        timeStr += '現在夜靈平原為夜晚，距離白天還有{:.0f}分鐘\n======\n'.format(nexttimeDelta-100)
    else:
        timeStr += '現在夜靈平原為白天，距離夜晚還有{:.0f}分鐘\n======\n'.format(nexttimeDelta)

    
    delta = datetime.timedelta(minutes = 150)
    for i in range(COUNT - 1):
        nexttime += delta
        timeList.append(nexttime)
    
    timeStr += '夜靈出現時間:\n'
    for time in timeList:
        timeStr += '{:0>4d}-{:0>2d}-{:0>2d} {:0>2d}:{:0>2d}\n'.format(time.year,time.month,time.day,time.hour,time.minute)

    await ctx.send(timeStr)
bot.run(jdata['TOKEN'])
