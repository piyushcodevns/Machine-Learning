def normalized(text):
    replacement={
        "ai":"artificial intelligance",
        "ml":"machine learning",
        "nlp":"natural language programming"
    }
    words=text.lower().split()
    normalized=[replacement.get(w,w)for w in words]
    return " ".join(normalized)

text="I want to learn ai and ml"
print(normalized(text))