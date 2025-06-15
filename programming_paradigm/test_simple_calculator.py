import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method with various cases."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)

    def test_subtraction(self):
        """Test the subtract method with various cases."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-5, -7), 2)
        self.assertEqual(self.calc.subtract(2.5, 1.5), 1.0)

    def test_multiplication(self):
        """Test the multiply method with various cases."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-3, -6), 18)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)

    def test_division(self):
        """Test the divide method with normal and edge cases."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertIsNone(self.calc.divide(10, 0))  # Division by zero returns None

if __name__ == "__main__":
    unittest.main()

