document=["python ai","python ml","ai nlp"]
vocabulary=["python","ai","ml","nlp"]
matrix=[]
for doc in document:
    word=doc.split()
    vector=[]
    for vocab in vocabulary:
        vector.append(word.count(vocab))
    matrix.append(vector)
print(matrix)