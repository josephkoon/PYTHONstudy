import threading



#function to thread
def addNum(start, end):
	total = 0
	
	for i in range(start,end):
		total = total + i
		
	return total
		

#create a list of the threads
Threads = []
	


#download multiple files at the same time to speed it up
for i in range(0,1400,100):

	#creates a thread object 
	addThread = threading.Thread(target=addNum, args=(i, i+99))
	
	#append to the list
	Threads.append(addThread)
	
	#starts the adding
	downloadThread.start()
	
print(Threads)


#add up a bunch of values at once, but much faster






