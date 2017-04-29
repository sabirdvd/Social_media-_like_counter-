from nltk import word_tokenize
from nltk.collocations import BigramCollocationFinder
text = "obama says that obama says that the war is happening"
finder = BigramCollocationFinder.from_words(word_tokenize(text))
finder.items()[0:5]

