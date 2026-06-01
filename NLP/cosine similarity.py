# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# sentence=[
#     "I like machine learning",
#     "I enjoy learning AI",
#     "The cat iis sleeping"
# ]

# vectorizer=CountVectorizer()
# vectors=vectorizer.fit_transform(sentence)
# similarity=cosine_similarity(vectors)

# print(vectorizer.get_feature_names_out())
# print(vectors.toarray())
# print(similarity)
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

student_question = "Ram goes to school"

lesson_titles = [
    "Python for AI and Machine Learning",
    "Introduction to HTML and CSS",
    "Sorting algorithms in Python",
    "How to deploy Angular on GitHub Pages",
    "Natural Language Processing basics"
]

all_texts = [student_question] + lesson_titles

vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(all_texts)

scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

best_index = scores.argmax()
best_lesson = lesson_titles[best_index]

print("Student question:")
print(student_question)
print(best_lesson)