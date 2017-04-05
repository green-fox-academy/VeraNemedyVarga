import unittest
from vera_nemedyvarga_work import *

class TestApple(unittest.TestCase):
    def test_get_apple(self):
        apple = Apple()
        self.assertEqual(apple.get_apple(), "apple")

class TestSum(unittest.TestCase):
    def test_sumall(self, integers = []):
        summa = Sum()
        integers = [3, 4, 5]
        self.assertEqual(summa.sumall(integers), 12)

    def test_sumall_empty_list(self, integers = []):
        summa = Sum()
        integers = []
        self.assertEqual(summa.sumall(integers), 0)

    def test_sumall_one_element_list(self, integers = []):
        summa = Sum()
        integers = [8]
        self.assertEqual(summa.sumall(integers), 8)

    def test_sumall_zero_inlist(self, integers = []):
        summa = Sum()
        integers = [0]
        self.assertEqual(summa.sumall(integers), 0)

if __name__ == '__main__':
    unittest.main()
