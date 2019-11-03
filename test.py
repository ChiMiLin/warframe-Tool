import datetime
COUNT = 10
locationPoint = datetime.datetime(2019,11,3,1,00,00)
now = datetime.datetime.now()
now_noSec = datetime.datetime(now.year,now.month,now.day,now.hour,now.minute)
zz = now_noSec - locationPoint
print(zz.seconds/60 + zz.days*24*60)

timeList = []
nexttime = now_noSec
count = 0
#找到下一個夜靈出沒定位點
for i in range(150):
    delta = datetime.timedelta(minutes = i)
    nexttime = now_noSec + delta
    delta = nexttime - locationPoint
    if (delta.seconds/60 + delta.days*24*60) % 150 == 0:
        timeList.append(nexttime)
        count += 1
        break

delta = datetime.timedelta(minutes = 150)
for i in range(COUNT - 1):
    nexttime += delta
    timeList.append(nexttime)
timeStr = ''
timeStr += '夜靈出現時間:\n'
for time in timeList:
    timeStr += '{:0>4d}-{:0>2d}-{:0>2d} {:0>2d}:{:0>2d}\n'.format(time.year,time.month,time.day,time.hour,time.minute)

print(timeStr)