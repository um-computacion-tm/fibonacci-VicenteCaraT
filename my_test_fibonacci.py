import unittest
from funcion_fibonacci import fibonacci_1


class TestFibonacci(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, fibonacci_1(1))

    def test_2(self):
        self.assertEqual(1, fibonacci_1(2))

    def test_3(self):
        self.assertEqual(2, fibonacci_1(3))

    def test_4(self):
        self.assertEqual(3, fibonacci_1(4))

    def test_5(self):
        self.assertEqual(5, fibonacci_1(5))

    def test_6(self):
        self.assertEqual(8, fibonacci_1(6))
        
        
if __name__ == '__main__':
    unittest.main()