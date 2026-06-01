import string
from nltk.stem import WordNetLemmatizer

sentence=[
    "Hello!!! I want to learn AI, Ml and NLP...",
    "Python teaches ML",
    "Champak Roy teaches NLP"
]
lemmetizer=WordNetLemmatizer()

def clean_text(text):
    text=text.lower()
    text="".join(ch for ch in text if ch not in string.punctuation)
    text=" ".join(text.split())
    words=[lemmetizer.lemmatize(w)for w in text.split()]
    return " ".join(words)

cleaning_sentence=[clean_text(s) for s in sentence]
print(cleaning_sentence)



vocab=[]
for s in cleaning_sentence:
    for word in s.split():
        vocab.append(word)
print(vocab)


matrix=[]
for s in cleaning_sentence:
    words=s.split()
    vector=[]
    for v in vocab:
        vector.append(words.count(v))
    matrix.append(vector)
print(matrix)


sentences=["Hello I want to learn python"]
words=sentences[0].split()
vector=[]
for v in vocab:
    if v in words:
        vector.append(1)
    else:
        vector.append(0)
print(vector)