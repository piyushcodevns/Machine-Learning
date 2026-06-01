import string
from nltk.stem import WordNetLemmatizer

lemmatizer=WordNetLemmatizer()
def clean_text(text):
    text=text.lower()
    text="".join(ch for ch in text if ch not in string.punctuation)
    text=" ".join(text.split())
    words=[lemmatizer.lemmatize(w)for w in text.split()]
    return words

message="Hello!!! I want to Learn AI, ML, and NLP..."
print(clean_text(message))