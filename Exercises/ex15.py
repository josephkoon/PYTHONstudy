#reading files with filename

from sys import argv

#get a filename from command line
script, filename = argv

#open the file
txt = open(filename)

print "Here is your file %r:" % filename

#use read command on the opened text file
print txt.read()

txt.close()

#as for file name within file
print "Type the filename again:"
file_again = raw_input("> ")

#open file 
txt_again = open(file_again)

#print contents of file
print txt_again.read()

txt_again.close()