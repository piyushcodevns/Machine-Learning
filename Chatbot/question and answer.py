import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# CSV Read
df = pd.read_csv(r"e:\Machine Learning\Chatbot\ml.csv")

print("===== Machine Learning Chatbot =====")

# Topics
topics = df["Topic"].astype(str).tolist()

# Vectorizer
vectorizer = TfidfVectorizer()

# Topic vectors
topic_vectors = vectorizer.fit_transform(topics)

while True:
    question = input("\nAsk Question: ").lower()

    if question == "exit":
        print("Chatbot Closed")
        break

    # Question vector
    question_vector = vectorizer.transform([question])

    # Similarity
    similarity = cosine_similarity(question_vector, topic_vectors)

    # Best match
    best_match = similarity.argmax()

    # Score
    score = similarity[0][best_match]

    if score > 0.2:

        print("\nTopic:", df.loc[best_match, "Topic"])

        print("\nDefinition:")
        print(df.loc[best_match, "Definition"])

        print("\nExample:")
        print(df.loc[best_match, "Example"])

        print("\nSimilarity Score:", round(score, 2))

    else:
        print("No answer found") 