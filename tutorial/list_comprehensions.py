# List Comprehensions is a very powerful tool,
# which creates a new list based on another list,
# in a single, readable line.

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)
