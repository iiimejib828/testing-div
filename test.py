import unittest
from main import remainder

class TestDivide(unittest.TestCase):
    def test_reminder_success(self):
        self.assertEqual(remainder(17, 3), 2)
        self.assertEqual(remainder(9, 4), 1)
        self.assertEqual(remainder(70, 14), 0)

    def test_reminder_by_zero(self):
        self.assertRaises(ValueError, remainder, 6, 0)

if __name__ == '__main__':
    unittest.main()
