class Girl:
	#class variable. every girl is female by default
	gender = "female"
	
	#instance variable unique to instance
	def __init__(self, name):
		self.name = name
	
	def ellasays(self):
		print("go away joey")
		
Ella = Girl("Ella")
Ella.ellasays()
	


