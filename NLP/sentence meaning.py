import re
from nltk.corpus import wordnet as wn

def clean_words(sentence):
    sentence = sentence.lower()
    return re.findall(r"[a-z]+", sentence)

def synonyms_of(word):
    result = {word}

    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            name = lemma.name().lower().replace("_", " ")
            result.add(name)

    return result

def antonyms_of(word):
    result = set()

    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            for antonym in lemma.antonyms():
                name = antonym.name().lower().replace("_", " ")
                result.add(name)

    return result

def expand_sentence(sentence):
    expanded = set()

    for word in clean_words(sentence):
        expanded.update(synonyms_of(word))

    return expanded

def find_antonym_conflicts(sentence1, sentence2):
    words1 = clean_words(sentence1)
    words2 = clean_words(sentence2)

    conflicts = []

    for w1 in words1:
        antonyms = antonyms_of(w1)
        for w2 in words2:
            if w2 in antonyms:
                conflicts.append((w1, w2))

    return conflicts

def meaning_match(sentence1, sentence2):
    expanded1 = expand_sentence(sentence1)
    expanded2 = expand_sentence(sentence2)

    common = expanded1.intersection(expanded2)
    total = expanded1.union(expanded2)

    synonym_score = 0
    if total:
        synonym_score = len(common) / len(total)

    conflicts = find_antonym_conflicts(sentence1, sentence2)

    final_score = synonym_score - (0.15 * len(conflicts))

    return synonym_score, conflicts, final_score, common

s1 = input("Enter first sentence: ")
s2 = input("Enter second sentence: ")

synonym_score, conflicts, final_score, common = meaning_match(s1, s2)

print("\nSentence 1:", s1)
print("Sentence 2:", s2)

print("\nSynonym expansion score:", round(synonym_score, 3))

print("\nCommon meaning words:")
for word in sorted(common):
    print("-", word)

print("\nAntonym conflicts:")
if conflicts:
    for pair in conflicts:
        print("-", pair[0], "opposes", pair[1])
else:
    print("No direct antonym conflict found.")

print("\nFinal meaning score:", round(final_score, 3))

if final_score > 0.20:
    print("Result: Sentences may be meaningfully related.")
elif final_score < 0:
    print("Result: Sentences may contain opposite meaning.")
else:
    print("Result: Weak or unclear relationship.")