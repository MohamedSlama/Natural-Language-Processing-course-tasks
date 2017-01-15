import nltk
import re
from collections import Counter

def cls():
    for i in range(50):
        print()


def edit_distance(s1, s2):
    m=len(s1)+1
    n=len(s2)+1

    tbl = {}
    for i in range(m): tbl[i,0]=i
    for j in range(n): tbl[0,j]=j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)

    return tbl[i,j]


def getRaw():
    raw = nltk.corpus.gutenberg.raw('shakespeare-hamlet.txt')
    return raw

def getTokens(raw):
    tokens = nltk.word_tokenize(raw)
    return tokens

#def Lemmatizer(Tokens):
#    wnl=nltk.WordNetLemmatizer()
#    lemma = [wnl.lemmatize(t) for t in Tokens]
#    return lemma


#def getSteamer(raw):
#    porter = nltk.PorterStemmer()
#    li = [porter.stem(t) for t in raw]
#    return li

def main():

    text1 = getRaw()
    #text2 = '''The Tragedie of Hamlet by
    #William Shakespeare Actus Primus. Scoena Prima.\n\nEnter Barnardo a'''
    text2 = '''The Tragedie of Hamle by illiam Shakespea'''
  
    tokens1 = list(set(getTokens(text1)))
    tokens2 = getTokens(text2)

    dic ={}
    key = 0
    for i in tokens2:
        SimilarWords = [w for w in tokens1 if re.search(i,w)]
        Words = [w for w in SimilarWords if edit_distance(w,i) <= 2]
        dic[key] = Words
        key += 1

    MaxVal =0
    MaxStr =0
    NewText=tokens2
    for i in range(1,len(dic)):
        for j in dic[i]:
            tx = NewText[i-1] + ' ' + j
            num = text1.count(tx) / text1.count(NewText[i-1])
            if num == 0: num = 1/len(text1)
            if num > MaxVal:
                MaxVal = num
                MaxStr = j
        NewText[i] = MaxStr
        MaxVal =0
        MaxStr =0
    return " ".join(NewText)
print(main())
