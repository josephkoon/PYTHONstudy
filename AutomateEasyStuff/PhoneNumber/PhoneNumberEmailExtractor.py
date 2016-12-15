import re

#match complex phone number regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # optional area code
    (\s|-|\.)?                        # separator of . or -
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator of . or -
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # spaces extension and numbers
    )''', re.VERBOSE)
	
	
	
#read the text
filename = input("Enter the filename: ")
text = open(filename, 'r').read()


#for all matching groups in the text
match = phoneRegex.findall(text)
print(match[0][0])


for i in range(len(match)):
	print(match[i][0])



	



