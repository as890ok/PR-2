import unittest

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        a, b = 2, 3
        result = a + b
        self.assertEqual(result, 5)

    def test_square(self):
        a = 4
        result = a ** 2
        self.assertEqual(result, 16)
    def test_cube(self):
        a = 3
        result = a ** 3
        self.assertEqual(result, 27)

if __name__ == '__main__':
    unittest.main()
