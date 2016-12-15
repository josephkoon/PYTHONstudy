#	\d\d\d-\d\d\d-\d\d\d\d

#	\d{3}-\d{3}-\d{4}


import re

#r means raw string which does not include string characters
#this creates a regular expression pattern of digits
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#this searches the statement for the pattern
mo = phoneNumRegex.search('My number is 555-555-4242.')

#
print(mo)

