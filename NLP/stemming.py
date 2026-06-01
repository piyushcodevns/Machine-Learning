from nltk.stem import PorterStemmer

stemmer=PorterStemmer()
words=["learning","classes","running","played"]
stemmed=[stemmer.stem(w)for w in words]
print(stemmed)