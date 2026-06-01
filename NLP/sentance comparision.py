from nltk.corpus import wordnet as wn
import re

def clean_words(sentence):
    sentence = sentence.lower()
    return re.findall(r"[a-z]+", sentence)

def synonyms_of(word):
    words = {word}

    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            words.add(lemma.name().lower().replace("_", " "))

    return words

def expanded_sentence_words(sentence):
    result = set()

    for word in clean_words(sentence):
        result.update(synonyms_of(word))

    return result

def sentence_meaning_score(sentence1, sentence2, sentence3):

    words1 = expanded_sentence_words(sentence1)
    words2 = expanded_sentence_words(sentence2)
    words3 = expanded_sentence_words(sentence3)

    common = words1.intersection(words2, words3)
    total = words1.union(words2, words3)

    if not total:
        return 0, common

    score = len(common) / len(total)

    return score, common

s1 = "I Love python"
s2 = "I love C"
s3 = "I love Java"

score, common_words = sentence_meaning_score(s1, s2, s3)

print("Sentence 1:", s1)
print("Sentence 2:", s2)
print("Sentence 3:", s3)

print("Meaning score:", round(score, 3))