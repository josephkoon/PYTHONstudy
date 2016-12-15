#import libraries random and url which opens URL
import random
from urllib import urlopen
import sys

#sets website equal to their website and creates an empty array for words
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

#writes out phrases for the text
PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

#look at user input if it is longer than 2 and is english that go to phrase
# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

#read lines from website and append to WORDS
#load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

#break the snippet into a question and answer and put variables into it
#takes the snippet and the phrase
def convert(snippet, phrase):
	#get a  class words from the WORDS list to replace in the snippet for the number of %%%
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    #get a random another names to replace with the ***
    other_names = random.sample(WORDS, snippet.count("***"))
    
    #create empty list for results and param names
    results = []
    param_names = []
	
	#for each of the @@@ in snippet : make a number from 1 to 3. replace with 1 to 3 of the words
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))
	
	#for the sentences in the snippet
    for sentence in snippet, phrase:
    	#copies the sentence to result
        result = sentence[:]

        # replace fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # replace fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # replace fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# keep going until they hit CTRL-D
try:
    while True:
    	#list all available keys in the PHRASES dict out of 5
        snippets = PHRASES.keys()
        #pick one of the snippets / key pairs at random
        random.shuffle(snippets)
		
		#for each of the snippets in the snippet
        for snippet in snippets:
        	#set the phrase equal to an instance
            phrase = PHRASES[snippet]
            #break the snippet into a question and answer and put variables into it
            question, answer = convert(snippet, phrase)
            
            
            if PHRASE_FIRST:
                question, answer = answer, question

            print question

            raw_input("> ")
            print "ANSWER:  %s\n\n" % answer
except EOFError:
    print "\nBye"