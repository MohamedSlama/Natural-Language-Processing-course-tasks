from nltk.book import *

def vocab_size(text):
    return len(text.split())
        
text = "mohamed abd elhamid mohamed moustfa"
Result = vocab_size(text)
print("The size is: " ,Result)