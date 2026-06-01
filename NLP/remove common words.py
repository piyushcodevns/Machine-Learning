sentence = "i want to learn python and ai with champak roy"

common_words = ["is", "in", "the", "a", "an", "and", "to", "of"]

words = sentence.lower().split()
important_words = []

for word in words:
    if word not in common_words:
        important_words.append(word)

print("All words:", words)
print("Important words:", important_words)