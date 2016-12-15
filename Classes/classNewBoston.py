class Enemy(object):
	life = 3
	
	#attack function to take life
	def attack(self):
		print("ouch!")
		self.life -= 1
	
	#checks life to see if it is less than 0
	def checkLife(self):
		if self.life <= 0:
			print("I am dead")
		else:
			print(str(self.life) + " life left")
		
	
vampire = Enemy()
vampire.attack()
vampire.checkLife()
vampire.attack()
vampire.checkLife()