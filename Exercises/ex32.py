#for loops

the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

#this for loop goes through a list
for number in the_count:
	print "this is count %d" % number
	
for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
#also notice we can have mixed lists
#we use %r since it could be a number of character
for i in change:
	print "I got %r" %i
	
elements = range(0,6)

#then use the range function to do 0 to 5 counts
#for i in range(0,6):
#	print "Adding %d to the list." % i
#	#append is a function that lists understand
#	elements.append(i)
	
print elements

#now print out the elements in that list
for i in elements:
	print "Element was: %d" % i