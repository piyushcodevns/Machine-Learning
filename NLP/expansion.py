import re
from nltk.corpus import wordnet as wn

lessons = [
    "Start Python from zero",
    "Begin machine learning with Python",
    "Introduction to Natural Language Processing",
    "HTML and CSS for beautiful web pages",
    "Deploy Angular website on GitHub Pages",
    "Text similarity using cosine similarity",
    "TF IDF search ranking in NLP"
]
def clean_words(text):
    return re.findall(r"[a-z]+", text.lower())
def expand_word(word):
    result = {word}
    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            result.add(lemma.name().lower().replace("_", " "))
    return result
def expand_text(text):
    expanded = set()
    for word in clean_words(text):
        expanded.update(expand_word(word))
    return expanded
def score(query, lesson):
    q = expand_text(query)
    l = expand_text(lesson)
    if not q or not l:
        return 0
    return len(q.intersection(l)) / len(q.union(l))
query = input("Search a lesson: ")
ranked = []
for lesson in lessons:
    ranked.append((lesson, score(query, lesson)))
ranked.sort(key=lambda item: item[1], reverse=True)
print("\nSearch:", query)
print("\nRanked lessons:")
for lesson, sc in ranked:
    print(round(sc, 3), "->", lesson)