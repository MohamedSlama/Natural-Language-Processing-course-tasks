import re
from nltk.corpus import *

def TextSearch(pattern,TestText):
	return [w for w in TestText if re.search(pattern,w)]

def getSortedWordList():
        return sorted(set(treebank.words()))


def hint():
        xx = '''ed$\n^..j..t..$\n^e-?mail$
^m+i+n+e+$\n^[he]+$\n^m*i*n*e*$\n^[A-Z]'''
        print( '\n===============\n' )
        print( xx )
        print( '\n===============\n' )

def cls():
        for i in range(10):
                print( '\n' )
