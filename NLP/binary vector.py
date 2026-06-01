vocabulary=["python","AI","ML","NLP"]
sentence="python NLP"
words=sentence.split()
vector=[]
for vocab_word in vocabulary:
    if vocab_word in words:
        vector.append(1)
    else:
        vector.append(0)
print(vector)