def palindrome_builder(word):
    print( word + word[::-1])
palindrome_builder('vera')

def is_palindrome(word):
    return word == word[::-1]

sentence = "dog goat dad duck doodle never"


def search_palindrome(sentence):
    palindromes = []
    for j in range(0, len(sentence)):
        for i in range(3, len(sentence)):
            if is_palindrome(sentence[j:(i + 1)]):
                if 3 <= len(sentence[j:(i + 1)]):
                    palindromes.append(sentence[j:(i + 1)])
    print(palindromes)

search_palindrome(sentence)


def anagram(word1, word2):
    #str to boolean
    for letter in word1:
        if letter in word2:
            return True
        else:
            return False

print(anagram("dog", "baba"))
print(anagram("god", "dog"))
