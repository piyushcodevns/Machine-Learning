from nltk.corpus import wordnet as wn

def word_similarity(word1, word2):
    synsets1 = wn.synsets(word1)
    synsets2 = wn.synsets(word2)

    if not synsets1 or not synsets2:
        return None

    # Beginner version:
    # take the first meaning of each word
    s1 = synsets1[0]
    s2 = synsets2[0]

    return s1.path_similarity(s2)

pairs = [
    ("car", "automobile"),
    ("dog", "cat"),
    ("happy", "sad"),
    ("big", "large"),
    ("book", "python")
]

for w1, w2 in pairs:
    score = word_similarity(w1, w2)
    print(w1, "-", w2, "=", score)