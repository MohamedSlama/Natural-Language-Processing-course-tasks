def getTokens():
    raw = """DENNIS: Listen, strange
women lying in ponds distributing swords
... is no basis for a system of government.
Supreme executive power derives from
... a mandate from the masses, not from some
farcical aquatic ceremony."""

    tokens = nltk.word_tokenize(raw)
    return tokens

def Lemmatizer(tokens):
    wnl=nltk.WordNetLemmatizer()
    print( [wnl.lemmatize(t) for t in tokens] )