"""
Word Occurrences
CP1404/CP5632 Practical
Estimate: 20 minutes
Actual: 39 minutes
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
for word, count in word_to_count.items():
    print(f"{word} : {count}")
