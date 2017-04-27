def is_anagram(word1, word2):
	if ''.join(sorted(word1)) == ''.join(sorted(word2)):
		print(True)
	else:
		print(False)

def is_palindrome(word):
    return word == word[::-1]

def search_palindrome(sentence):
    palindromes = []
    subsets = words_w_nchars(sentence)

    for word in subsets:
        if is_palindrome(word):
            palindromes.append(word)
    return palindromes

sentence = 'dog goat dad duck doodle never'

def words_w_nchars(word, n = 3):
    words = []
    length = len(word)
    for index in range(length):
        for l in range(n, length):
            if (l + index) <= length:
                words.append(word[index : (index + l)])
    return words

print(search_palindrome(sentence))
is_anagram("dog", "god")
