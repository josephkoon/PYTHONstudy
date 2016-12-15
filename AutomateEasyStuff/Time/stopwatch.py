#track the amount of time elapsed between presses of ENTER, each key starts a lap
#print the lap number, total time, and lap time

#find the current time by calling time.time() and store it 
#record the time at each start of the lap
#keep a lap counter and increment it every time the user presser enter
#calculate the elapsed time

#handle keyboard interupt so the user can quit with CTRL-c

import time

print('PRESS ENTER TO BEGIN. PRESS ENTER FOR EACH LAP')

raw_input()

startTime = time.time()
lastTime = startTime
laps = 0

while True:
	raw_input()
	lapTime = round(time.time() - lastTime)
	lastTime = time.time()
	laps += 1
	
	print('Lap Number : ' + str(laps))
	print('Lap Time : ' + str(lapTime))
	print('Total Time : ' + str(round(lastTime - startTime)))
	
	
	

