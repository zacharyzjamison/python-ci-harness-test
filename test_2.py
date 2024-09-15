import unittest

def subtract(a, b):
    return a - b

class TestSubtractFunction(unittest.TestCase):
    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(1, 2), -1)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-1, -2), 1)

    def test_subtract_mixed_numbers(self):
        self.assertEqual(subtract(1, -2), 3)
        self.assertEqual(subtract(-1, 2), -3)

if __name__ == '__main__':
    unittest.main()