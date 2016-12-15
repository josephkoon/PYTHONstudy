#threading to run multiple programs

import threading, time

print('Start of program')

def takeANap():
	time.sleep(5)
	print('Wake up!')
	
	
#create a thread object
threadObj = threading.Thread(target=takeANap)

#starts the thread with the takeANap function
threadObj.start()


print('End of program')







