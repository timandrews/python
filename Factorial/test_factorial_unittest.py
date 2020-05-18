import unittest
import math
import factorial



class TestFactorial(unittest.TestCase):
    def test_zero(self):
        result = factorial.my_factorial(0)
        self.assertEqual(result, math.factorial(0))

    def test_positive(self):
        result = factorial.my_factorial(10)
        self.assertEqual(result, math.factorial(10))

    def test_ValueError(self):
        with self.assertRaises(ValueError):
            factorial.my_factorial(-10)

    def test_TypeError(self):
        with self.assertRaises(TypeError):
            factorial.my_factorial('a string')
            factorial.my_factorial(1.5)

if __name__ == '__main__':
    unittest.main()
