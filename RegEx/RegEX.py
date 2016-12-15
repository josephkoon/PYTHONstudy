#	\d\d\d-\d\d\d-\d\d\d\d

#	\d{3}-\d{3}-\d{4}


import re

#r means raw string which does not include string characters
#.compile creates a regular expression pattern of digits
#phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#this searches the statement for the pattern
#mo = phoneNumRegex.search('My number is 555-555-4242.')

#.group() returns the result of the match as a string
#print(mo.group())


#phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#mo = phoneNumRegex.search('My number is 415-555-4242')
#mo.group(1) #returns first chunk
#mo.group(2) #returns second group
#mo.group(0) #returns whole thing
#mo.group()
#mo.groups() #returns all groups at once
#areaCode, mainNumber = mo.groups() #seperates the tuple groups out



#matching with parantheses (\
#phoneNumRegex = re.compile(r'(\(\d\d\d)) (\d\d\d-\d\d\d\d)')
#mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
#mo.group(1)
#mo.group(2)



#or regex with | pipe
#heroRegex = re.compile (r'Batman|Tina Fey')
#mo1 = heroRegex.search('Batman and Tiny Fey.')
#print(mo1.group())



#find one of a series of words
#batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
#mo = batRegex.search('Batmobile lost a wheel')
#print(mo.group())
#print(mo.group(1))



#finds Bat(wo)man with (wo) being optional
#batRegex = re.compile(r'Bat(wo)?man')
#mo1 = batRegex.search('The Adventures of Batman')
#print(mo1.group())



#mo2 = batRegex.search('The Adventures of Batwoman')
#print(mo2.group())



#finds a number without any area code. anything before the ? is optional
#phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
#mo1 = phoneRegex.search('My number is 415-555-4242')
#print(mo1.group())

#mo2 = phoneRegex.search('My number is 555-4242')
#print(mo2.group())



# * means match zero or more matches
#batRegex = re.compile(r'Bat(wo)*man')
#mo1 = batRegex.search('The Adventures of Batman')
#print(mo1.group())

#mo2 = batRegex.search('The Adventures of Batwoman')
#print(mo2.group())

#mo3 = batRegex.search('The Adventures of Batwowowowoman')
#print(mo3.group())



# the + means match 1 or more instances
#batRegex = re.compile(r'Bat(wo)+man')
#mo1 = batRegex.search('The Adventures of Batwoman')
#print(mo1.group())

#mo2 = batRegex.search('The Adventures of Batwowowowoman')
#print(mo2.group())

#mo3 = batRegex.search('The Adventures of Batman')
#mo3 == None


# match specific number of repetitions with {}
#(Ha){3} == 'HaHaHa'
#(Ha){3,5} == 'HaHaHa' or 'HaHaHaHa'
#(Ha){3,} == 'HaHaHa' or 'HaHaHaHaHaHa'
#(Ha){,5} == 'Ha'



#finds 3 instances of Ha with {}
#haRegex = re.compile(r'(Ha){3}')
#mo1 = haRegex.search('HaHaHa')
#print(mo1.group())

#mo2 = haRegex.search('Ha')
#mo2 == None


#non greedy match. finds the shortest match 
#nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
#mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
#mo2.group() = 'HaHaHa'



#find all. instead of finding first match, this finds all matches
#phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #no groups
#phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000') #finds both numbers


#find all with groups.
#phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') #no groups
#phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000') #finds both numbers
#[('415','555','9999'),('212','555','0000')]


#Character classes
#/d for number from 0 to 9
#/D for character that is not from 0 to 9
#/w for any letter, digit or underscore (matching word character)
#/W for any character that is not a letter, digit or underscore
#/s for any space, tab or newline character (matching space character)
#/S for any character that is not a space, tab or newline


#match any text that has 1 or more digitas followed by whitespace followed by one or more 
#digit / underscore
#xmasRegex = re.compile(r'\d+\s\w+')


#matching custom character classes
#vowelRegex = re.compile(r'[aeiouAEIOU]')
#vowelRegex = re.compile(r'[a-zE-Z0-9]')
#vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
#['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']


#match custom characters NOT inside
#consonantRegex = re.compile(r'[^aeiouAEIOU]')
#consonantRegex.findall('Robocop eats baby food. BABY FOOD.')
#['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', '
#', 'B', 'B', 'Y', ' ', 'F', 'D', '.']


# use ^ for specifying that it must start with this regex
#beginsWithHello = re.compile(r'^Hello')
#beginsWithHello.search('He said hello.') == None

# use $ to specify that it must end with this regex
#endsWithNumber = re.compile(r'\d$')
#endsWithNumber.search('Your number is 42')
#endsWithNumber.search('Your number is forty two.') == None

# use the ^\d+$' to match strings that match both beginning and end 
#wholeStringIsNum = re.compile(r'^\d+$')
#wholeStringIsNum.search('12345xyz67890') == None


#use the . as a wildcard to match any character except new line
#atRegex = re.compile(r'.at')
#atRegex.findall('The cat in the hat sat on the flat mat.')
#['cat', 'hat', 'sat', 'lat', 'mat']


# use .* to match anything
#nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
#mo = nameRegex.search('First Name: Al Last Name: Sweigart')


#use the .*? to match in a nongreedy way
#nongreedyRegex = re.compile(r'<.*?>')
#mo = nongreedyRegex.search('<To serve man> for dinner.>')
#mo.group() == '<To serve man>'


#use re.DOTALL to pass everything with newlines



# ? matches 0 or 1
# * matches 0 or more
# + matches 1 or more
# the {n} match exactly that many
# the {n,} matches n or more 
# the {,m} matches 0 to m
# the {n,m} matches atleast n and at most m
# the {n,m}? or *? or +? performs nongreedy match
# ^spam must begin with spam
# spam$ must end with spam
# the . matches any character except newline
# \d, \w, and \s match a digit, word or space
# \D, \W, and \S match anything except a digita, word or space
# [abc] matches any character between the brackets
# [^abc] matches any character not between the brackets

#use re.IGNORECASE or re.I to make it noncasesensitive
#robocop = re.compile(r'robocop', re.I)
#robocop.search('Robocop is part man, part machine, all cop.').group()
#'Robocop'


# switch one text for another text
#namesRegex = re.compile(r'Agent \w+')
#namesRegex.sub('CENSORED','Agent Alice gave the secret documents to Agent Bob.')
#replaces Anything with Agent and the next word 


#replace with first letters and other randoms
#agentNamesRegex = re.compile(r'Agent (\w)\w*')
#agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
#A**** told C**** that E**** knew B**** was a double agent.'

#use re.VERBOSE to write long regular expressions
#phoneRegex = re.compile(r'''(
#    (\d{3}|\(\d{3}\))?            # area code
#    (\s|-|\.)?                    # separator
#   \d{3}                         # first 3 digits
#    (\s|-|\.)                     # separator
#    \d{4}                         # last 4 digits
#    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
#    )''', re.VERBOSE)

#combine ignorecase dotall and verbose
#someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

