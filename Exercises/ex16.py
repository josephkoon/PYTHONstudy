from sys import argv

#take filename from command line
script, filename = argv

#print we are going to erase the file
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you want that, hit RETURN."

#ask for input
raw_input("?")

#opens the file
print "Opening the file..."
target = open(filename, 'w+')

#truncates the file
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

#ask for new lines of text
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#re write these lines into the text file
target.write(line1 + "\n" +line2 + "\n"+ line3)


#close the text file
print "And finally, we close it."
target.close()


text = open(filename, 'r')
print "Now I will read the file"
print text.read()
text.close()

