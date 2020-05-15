import unittest
import math
from factorial import my_factorial


class TestFactorial(unittest.TestCase):
    # def test_negative(self):
    #     pass

    def test_zero(self):
        result = my_factorial(0)
        self.assertEqual(result, math.factorial(0))

    def test_positive(self):
        result = my_factorial(10)
        self.assertEqual(result, math.factorial(10))

    def test_ValueError(self):
        self.assertRaises(ValueError, my_factorial, -10)

    def test_TypeError(self):
        self.assertRaises(TypeError, my_factorial, 'a string')
        self.assertRaises(TypeError, my_factorial, '1.5')


if __name__ == '__main__':
    unittest.main()
