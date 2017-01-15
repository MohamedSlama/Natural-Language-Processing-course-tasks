from nltk.book import *
from matplotlib import *

word = [w for w in text5 if len(w) ==4 and not w.isdigit()]
fdist = FreqDist(word)
fdist.plot(20,cumulative =True)