#copies data from one text file to the other
from sys import argv
from os.path import exists

script, from_file, to_file = argv

#sets in_file equal to the open file to open it
with open(from_file, 'r') as f:
	output = f.read()
	
out_file = open(to_file, 'w')

#reads the data from the file into indata
out_file.write(output)




