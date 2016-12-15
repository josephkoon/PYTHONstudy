import threading

class BuckyMessenger(threading, Thread):
	#special thread format
	def run(self):
		for _ in range(10):
			print(threading.currentThread().getName())
			
x = BuckyMessenger(name = "Send out messages")
y = BuckyMessenger(name = "Recieve messages")
x.start()
y.start()