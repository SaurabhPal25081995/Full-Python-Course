import datetime as dt
import time
a = dt.datetime(1970,1,1,0,0,0)
#b = dt.datetime(2013,12,31,23,59,59)
#c=time.asctime(time.localtime(time.time()))
d = dt.datetime.now()
print("d",d)
#print(c)
print((d-a).total_seconds())