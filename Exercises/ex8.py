formatter  = "%r %r %r %r"

#prints all of the variables
print formatter % (1,2,3,4)
#prints all of the variables again
print formatter % ("one", "two", "three", "four")
#prints all of the booleans
print formatter % (True, False, False, True)

print formatter % (formatter, formatter, formatter, formatter)


#prints all of the statements
print formatter % (
"I had this thing.", 
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight."
)