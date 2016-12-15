class Enemy:
	#initialize with energy variable
	def __init__(self, x, name):
		self.energy = x
		self.name = name
		
	def get_energy(self):
		print(str(self.name) +" has "+str(self.energy)+" energy")
		
		
Jason = Enemy(5, "Jason")
Sandy = Enemy(5, "Sandy")
Jason.get_energy()
Sandy.get_energy()



