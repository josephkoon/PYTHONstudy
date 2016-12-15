print "yes\\no" #backslash
print "yes\' no" #single quote
print 'yes\" no' #double quote
print "yes\ano" #BEL
print "yes\bno" #backspace
print "yes\fno" #formfeed
print "yes\nno" #line feed
print "yes\N{name}" #character named name 
print "yes\rno" #carriage return
print "yes\tno" #horizontal tab
print "yes\uxxxxxxno" #character with 16 bit hex
print "yes\U1011110101" #character with 32 bit hex
print "yes\vno" #ASCII vertical tab
print "yes\ooono" #char with octal value ooo


print '''
yes yes yes
no no no
'''

print """
yes yes yes
no no no
"""

#while True:
#	for i in ["/", "-", "|", "\\", "|"]:
#		print "%s\r" %i,