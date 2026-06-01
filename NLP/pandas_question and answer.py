import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = {
    "Questions": [
        "What is AI?",
        "What is Machine Learning?",
        "How are you?",
        "What is Python?",
    ]
}
df = pd.DataFrame(data)
user_question = input("Enter your question: ")
all_questions = df["Questions"].tolist()
all_questions.append(user_question)
cv = CountVectorizer()
vectors = cv.fit_transform(all_questions)
similarity = cosine_similarity(vectors)
scores = similarity[-1][:-1]
best_score = max(scores)
print("Matched Percentage:", round(best_score, 4))