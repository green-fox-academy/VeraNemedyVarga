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
        self.assertEqual(ana.anagram("", ""), True)

if __name__ == '__main__':
    unittest.main()
