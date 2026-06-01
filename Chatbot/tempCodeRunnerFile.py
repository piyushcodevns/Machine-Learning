from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import re

# LOAD DATA
file = open(r"e:\Machine Learning\Chatbot\ml.txt", "rb")
text = pickle.load(file)

# USER QUESTION
student_question = input("Ask Question: ").lower()

# SPLIT TEXT
lesson_titles = re.split(r'\n+', text)

# REMOVE BAD LINES
lesson_titles = [
    line.strip().lower()
    for line in lesson_titles
    if (" is " in line.lower()) and 40 < len(line.strip()) < 300
]

# COMBINE QUESTION + DATA
all_texts = [student_question] + lesson_titles

# VECTORIZE
vectorizer = TfidfVectorizer(stop_words="english")
vectors = vectorizer.fit_transform(all_texts)

# SIMILARITY
scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

# BEST ANSWER
best_index = scores.argmax()
best_answer = lesson_titles[best_index]

print("\nBest Answer:")
print(best_answer)