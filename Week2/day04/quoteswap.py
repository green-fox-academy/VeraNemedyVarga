# Accidentally I messed up this quote from Richard Feynman.
# Two words are out of place
# Your task is to fix it by swapping the right words with code

# Also, print the sentence to the output with spaces in between.

words = ["What", "I", "do", "create,", "I", "cannot", "not", "understand."]
a = words[2]
b = words[5]
words[5] = a
words[2] = b
print(words)
