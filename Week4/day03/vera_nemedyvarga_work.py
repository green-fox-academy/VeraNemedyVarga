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
        if ''.join(sorted(self.word1))==''.join(sorted(self.word2)):
            return True
        else:
            return False

# Write a function, that takes two strings and returns a boolean value based on if the two strings are Anagramms or not.
# Create a test for that.
