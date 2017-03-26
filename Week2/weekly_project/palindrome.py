"""a = "adika"

for letter in range(len(a)-1, -1, -1):
	print(a[letter])"""

# def create_palindrome(word):
#     return word + word[::-1]
#
# print(create_palindrome('malac'))
#
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

#
# for letter in sentence:
#     if len(word) >= 3:

# str, num -> list
# asda -> [asd, asda, sda]
def words_w_nchars(word, n = 3):
    words = []
    length = len(word)
    for index in range(length):
        for l in range(n, length):
            if (l + index) <= length:
                words.append(word[index : (index + l)])

    return words

print(search_palindrome(sentence))
