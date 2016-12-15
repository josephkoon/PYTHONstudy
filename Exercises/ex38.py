ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

#break stuff with spaces
stuff = ten_things.split(' ')

#new list of stuff
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

#while stuff list has less than 10 parts
while len(stuff) != 10:
#set next one equal to the last value of the other list
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	#add that value to stuff
	stuff.append(next_one)
	#print length of stuff
	print "There are %d items now." % len(stuff)
	
print "There we go: ", stuff
print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])
