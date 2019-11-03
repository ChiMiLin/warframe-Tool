import datetime

locationPoint = datetime.datetime(2019,11,2,23,00,00)
now = datetime.datetime.now()
now_noSec = datetime.datetime(now.year,now.month,now.day,now.hour,now.minute)
after = now - locationPoint

#找到下一個夜靈出沒定位點
for i in range(150):
    delta = datetime.timedelta(seconds = i*60)
    nexttime = now_noSec + delta
    if ((nexttime - locationPoint).seconds/60) % 150 == 0:
        print(nexttime)
        break