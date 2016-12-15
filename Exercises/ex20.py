from sys import argv

script, input_file = argv

#print everything inside a file
def print_all(f):
	print f.read()
	
#sets the file backwards
def rewind(f):
	f.seek(0)
	
#print a single line from the file
def print_a_line(line_count, f):
	print line_count, f.readline()
	
#open the inputted file
current_file = open(input_file)

print "First let's print the while file:\n"
print_all(current_file)

print "now let's rewind, kind of like a tape."
rewind(current_file)

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
