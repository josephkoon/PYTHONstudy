import time, subprocess

timeLeft = 4

while timeLeft > 0:
	print(timeLeft)
	time.sleep(1)
	timeLeft = timeLeft - 1
	
subprocess.Popen(['open', 'hello.txt'])