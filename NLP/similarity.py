from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sentences = [
    "Piyush cooks maggie",
    "piyush cooked maggie"
]

vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(sentences)
similarity = cosine_similarity(vectors[0], vectors[1])
print(similarity)