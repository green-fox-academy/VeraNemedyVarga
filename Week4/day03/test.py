import unittest
import extend

class TestExtend(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_7_and_6_is_13(self):
        self.assertEqual(extend.add(7, 6), 13)

    def test_add_4_and_5_is_9(self):
        self.assertEqual(extend.add(4, 5), 9)

    def test_max_of_three_first(self):
        self.assertEqual(extend.max_of_three(8, 8, 5), 8)

    def test_max_of_three_third(self):
        self.assertEqual(extend.max_of_three(17, 12, 15), 15)

    def test_median_four(self):
        self.assertEqual(extend.median([7,6,3,4]), 5)

    def test_median_five(self):
        self.assertEqual(extend.median([1,2,2,4,5]), 3)

    def test_is_vovel_a(self):
        self.assertTrue(extend.is_vovel('ú'))

    def test_is_vovel_u(self):
        self.assertTrue(extend.is_vovel('ä'))

    def test_translate_bemutatkozik(self):
        self.assertEqual(extend.translate('bavaria'), 'bavavarivia')

    def test_translate_kolbice(self):
        self.assertEqual(extend.translate('revolver'), 'revevovolvever')

if __name__ == '__main__':
    unittest.main()
