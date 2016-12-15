#date time

import datetime
import time


#nice formating for dates (%Y, %y, %m, %B, %d, %j, %w, %A, %a, %H, %I, %M, %S, %P, %%)
oct21st = datetime.datetime(2015, 10,21,16,29,0)
oct21st.strftime('%Y/%m/%d %H:%M:%S)

#convert back to datetime
datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')



#year, month, day, hour, minute, second, microsecond
datetime.datetime.now()

dt = datetime.datetime

dt.year
dt.month
dt.day

dt.hour
dt.minute
dt.second


datetime.datetime.fromtimestamp(time.time())
#datetime.datetime(2015, 2, 27, 11, 13, 0, 604980)


#time duration
delta = datetime.delta(days=11, hours=10, minutes=9, seconds =8)
delta.days
delta.seconds
delta.microseconds

delta.total_seconds()
st(delta)


#add times with durations
dt = datetime.datetime.now()
thousandDays = datetime.timedelta(days=1000)
dt = dt + thousandDays


#pause until halloween
halloween2016 = datetime.datetime(2016, 10,31,0,0,0)
while datetime.datetime.now() < halloween2016 :
	time.sleep(1)
	






