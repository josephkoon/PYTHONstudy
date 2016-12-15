from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	#ask for how much gold, if it is 0 or 1 then set that to the value
	choice = raw_input("> ")
	if int(choice)>0:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")
		
	#if amount entered is less than, 50 exit
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")
		
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	#keep asking to input. can enter take honey, or taunt bear
	#entering take honey kills you
	#entering taunt bear moves the bear
	#entering open door goes into gold room
	#else asks again for value
	while True:
		choice = raw_input("> ")
		
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through."
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."
			
def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for you life or eat your head?"
	
	#ask for input. if flee go to start
	#if head. die
	#else ask again for input
	choice = raw_input("> ")
	
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()
		
def dead(why):
	#whenever death occurs, print reason and exit
	print why, "Good job!"
	exit(0)
	
def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	#initial questions 
	#turn left goes to bear room
	#turn right goes to cthulu
	choice = raw_input("> ")
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulu_room()
	else:
		dead("You stumble around the room until you starve.")
		
start()
		
	
		
		
			
			
	