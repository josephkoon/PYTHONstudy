print "You enter a dark room with two doors. Do you go through door 1 or door 2?"

door = raw_input("> ")

if door == "1":
	print "There is a giant bear. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off."
	elif bear == "2":
		print "The bear eats your leg off."
	else:
		print "Well doing %s is probably better. Bear runs away." % bear
		
elif door == "2":
	print "You stare into the endless abyss."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by jello."
	else:
		print "The insanity rots your eyes into muck."
		
else:
	print "You stumble on a knife and die."