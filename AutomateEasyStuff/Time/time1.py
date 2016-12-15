#look at duration of time

import time

def calcProd():
	#calculate the product of the first 100,000 numbers
	product = 1
	for i in range(1,100000):
		product = product * i
	return product
	
#calc time, run function, calc time again
startTime = time.time()
prod = calcProd()
endTime = time.time()

print('it took %s seconds to calculate' %(endTime - startTime))

#also see cProfile.run()

