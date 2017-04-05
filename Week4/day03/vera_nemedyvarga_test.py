import unittest
from vera_nemedyvarga_work import *

class TestApple(unittest.TestCase):
    def test_get_apple(self):
        apple = Apple()
        self.assertEqual(apple.get_apple(), "apple")

class TestSum(unittest.TestCase):
    def test_sumall(self):
        summa = Sum()
        self.assertEqual(summa.sumall([3, 4, 5]), 12)

    def test_sumall_empty_list(self):
        summa = Sum()
        self.assertEqual(summa.sumall([]), 0)

    def test_sumall_one_element_list(self):
        summa = Sum()
        self.assertEqual(summa.sumall([8]), 8)

    def test_sumall_zero_inlist(self):
        summa = Sum()
        self.assertEqual(summa.sumall([0]), 0)

class TestAnagram(unittest.TestCase):
    def test_anagram(self):
        ana = Anagram()
        self.assertEqual(ana.anagram("alma", "mlaa"), True)

class TestCountLetters(unittest.TestCase):
    def test_countletters(self):
        newword = CountLetters()
        word = "alma"
        self.assertEqual(newword.countletters(word), {'m':1, 'l':1, 'a':2 })

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        fibo = Fibonacci()
        self.assertEqual(fibo.fibonacci(6), 8)

    def test_fibonacci(self):
        fibo = Fibonacci()
        self.assertEqual(fibo.fibonacci(0), 0)

    def test_fibonacci(self):
        fibo = Fibonacci()
        self.assertEqual(fibo.fibonacci(1), 1)

    def test_fibonacci(self):
        fibo = Fibonacci()
        self.assertEqual(fibo.fibonacci(2), 1)

    def test_fibonacci(self):
        fibo = Fibonacci()
        self.assertEqual(fibo.fibonacci(3), 2)
if __name__ == '__main__':
    unittest.main()
