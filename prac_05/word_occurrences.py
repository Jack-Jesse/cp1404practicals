"""
Word Occurrences
CP1404/CP5632 Practical
Estimate: 20 minutes
Actual: 32 minutes
A program that prints the number of times a word in text shows appears.
"""

text = "this is a collection of words of nice words this is a fun thing it is"
word_to_count = {}
words = sorted(text.split())
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
max_length = max(len(word) for word in word_to_count)
for word, count in word_to_count.items():
    print(f"{word:{max_length}} : {count}")
