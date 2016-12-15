from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#sets in_file equal to the open file to open it
in_file = open(from_file, 'r')

#reads the data from the file into indata
indata = in_file.read()

#prints size of read file
print "The input file is %d bytes long" % len(indata)

#prints if the file exists or not
print "Does the output file exist? %r" % exists(to_file)
print "Read, hit RETURN to continue, CTRL-C to abort."
raw_input()

#opens the out going file
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()



