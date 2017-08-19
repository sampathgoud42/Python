from datetime import datetime
import time
time_stamp= datetime.now()
print(datetime.utcnow())
print (time_stamp)

print (time_stamp.year)
print (time_stamp.month)
print (time_stamp.day)
now= datetime.utcnow()
print ('%s/%s/%s' % (now.month, now.day, now.year))
print ('%s-%s-%s' % (now.day, now.month, now.year))
print (now.hour)
print (now.minute)
print (now.second)
print (now.tzinfo)
print (now.fold)

epoch=((datetime(now.year,now.month,now.day,now.hour,now.minute,now.second,now.microsecond) - datetime(1970,1,1)).total_seconds())
print (epoch)

print (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch)))

# print ('%s:%s:%s' % (now.hour, now.minute, now.second))
