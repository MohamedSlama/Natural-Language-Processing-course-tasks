def getRaw():
    raw = """DENNIS: Listen, strange
women lying in ponds distributing swords
... is no basis for a system of government.
Supreme executive power derives from
... a mandate from the masses, not from some
farcical aquatic ceremony."""

    return raw

def Tokenizer(text):
    sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    #text=nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
    sents=sent_tokenizer.tokenize(text)
    print( sents )