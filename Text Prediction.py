import nltk
import re
from collections import Counter

def Tokenizer():
    sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    text=nltk.corpus.gutenberg.raw('shakespeare-hamlet.txt')
    sents=sent_tokenizer.tokenize(text)
    return sents

#def GetGutenbergTextName():
#    print (nltk.corpus.gutenberg.fileids())    

def Predition(text):
    txt = Tokenizer()
    ser = [w for w in txt if re.search(text,w)]
    
    if len(ser) == 0:
        print( 'Not Fount' )
    
    li_w = []
    for sentence in ser:
        tokens = nltk.word_tokenize(sentence)
        for j in range(len(tokens)):
            word = text + ' ' + tokens[j]
            Temp = sentence.find(word)
            if Temp != -1:
                li_w.append(word)

    c = [ite for ite, it in Counter(li_w).most_common(3)]
    print(c)
    
        

Predition('is')
