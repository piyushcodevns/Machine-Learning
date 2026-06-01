from nltk.stem import WordNetLemmatizer

lemmatizer=WordNetLemmatizer()
words=["children", "better", "running", "studies"]

lemmatized=[lemmatizer.lemmatize(w)for w in words]
print(lemmatized)