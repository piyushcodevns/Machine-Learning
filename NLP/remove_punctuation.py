import string

text = "Hello!!! Do you teach AI, ML, and NLP???"

clean = "".join(ch for ch in text if ch not in string.punctuation)
print(clean)
