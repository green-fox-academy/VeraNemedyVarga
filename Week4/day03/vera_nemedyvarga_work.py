class Apple(object):
    def get_apple(self):
        return "apple"

class Sum():
    def sumall(self, integers = []):
        self.integers = integers
        return sum(self.integers)

class Anagram():
    def anagram(self, word1, word2):
        self.word1 = word1
        self.word2 = word2
        if ''.join(sorted(self.word1)) ==''.join(sorted(self.word2)):
            return True
        else:
            return False

class CountLetters():
    def countletters(self, word):
        self.word = word
        self.keylist = []
        self.valuelist = []
        self.dicti = {}
        for letter in word:
            self.keylist.append(letter)
            self.valuelist.append(self.word.count(letter))
        for key, value in zip(self.keylist, self.valuelist):
            self.dicti[key] = value
        return self.dicti

class Fibonacci():
    def fibonacci(self, number):
        self.number = number
        if self.number == 0:
            return 0
        elif self.number==1:
            return 1
        else:
            return self.fibonacci(number-1) + self.fibonacci(number-2)


# Write a function that computes a member of the fibonacci sequence by a given index
# Create tests that covers all types of input (like in the previous workshop exercise)
