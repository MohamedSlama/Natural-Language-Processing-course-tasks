import nltk.stem.porter



def getTokens():
    raw = """DENNIS: Listen, strange
women lying in ponds distributing swords
... is no basis for a system of government.
Supreme executive power derives from
... a mandate from the masses, not from some
farcical aquatic ceremony."""

    tokens = nltk.word_tokenize(raw)
    return tokens

def Stemmer(Name,tokens):
    
    if Name.lower() == 'porter':
        print('======== Porter Stemmer ======\n\n')
        porter = nltk.PorterStemmer()
        print( [porter.stem(t) for t in tokens] )
    elif Name.lower() == 'lancaster':
        print('======== Lancaster Stemmer ======\n\n')
        lancaster = nltk.LancasterStemmer()
        print( [lancaster.stem(t) for t in tokens] )

    else:
        print('======== Undefine ======\n\n')