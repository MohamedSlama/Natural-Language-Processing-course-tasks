from nltk.book import *

Summation = sum([len(w) for w in text1]) # This line get the length of every word in "text1"
                                   # then get the summation of these lengths 
Length    = len(text1)
Average   = Summation / Length 
print("The average is: " + str(Average))