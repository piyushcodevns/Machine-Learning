sentences=[
    "Python AI",
    "Python ML",
    "Champak Roy NLP"
]
vocabulary=[]
for sentence in sentences:
    words=sentence.split()
    for word in words:
        if word not in vocabulary:
            vocabulary.append(word)
print(vocabulary)