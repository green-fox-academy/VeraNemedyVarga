class Apple(object):
    def get_apple(self):
        return "apple"

class Sum():
    def sumall(self, integers = []):
        self.integers = integers
        return sum(self.integers)
