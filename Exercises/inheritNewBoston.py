class Parent():
	def print_last_name(self):
		print("Roberts")
		
#look for a parent class and pass it to child
class Child(Parent):
	def print_first_name(self):
		print("Bucky")
	
	#over write other last name
	def print_last_name(self):
		print("Burger")
		
	
bucky = Child()
bucky.print_first_name()
bucky.print_last_name()


	
