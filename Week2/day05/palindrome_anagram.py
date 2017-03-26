#Build palindrome from word
def palindrome_builder(word):
    print( word + word[::-1])
palindrome_builder('vera')

#Check if word is palindrome
def is_palindrome(word):
    return word == word[::-1] #check if reverse is the same as original


#text example
sentence = "dog goat dad duck doodle never"
palindromes = []

#Palindromes in sentence finder
for j in range(0, len(sentence)):   #iterate over first index of sentence slice
    for i in range(3, len(sentence)):   #iterate over second index
        if is_palindrome(sentence[j:(i + 1)]):  #call is_palindrome on slice
            if 3 <= len(sentence[j:(i + 1)]):   #only selects the ones with length 3 or over
                palindromes.append(sentence[j:(i + 1)])     #adds it to a list

print(palindromes)

#Anagram
def anagram(word1, word2):
    #str to boolean
    for letter in word1:
        if letter in word2:
            return True
        else:
            return False

print(anagram("dog", "baba"))       #test, should print False
print(anagram("god", "dog"))        #test, should print True
