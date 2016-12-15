#string formatting

#sets x = to...
x = "There are %d types of people." %10
#sets binary = to....
binary = "binary"
#sets do_not = to....
do_not = "don't"
#replaces values with other values
y = "Those who know %s and those who %s." % (binary, do_not)

#prints statements
print x
print y

#prints statement by filling in other values
print "I said: %r." % x
#prints statement by filling in additional values
print "I also said: '%s'." % y

#prints statement by replacing other value
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#prints full sentence
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#adds left and right side
print w + e