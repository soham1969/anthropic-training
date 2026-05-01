import unittest
from main import calculate_pi_to_5th_digit


class TestPiCalculation(unittest.TestCase):
    """Test cases for pi calculation function"""
    
    def test_pi_to_5th_digit(self):
        """Test that pi is calculated correctly to the 5th decimal place"""
        result = calculate_pi_to_5th_digit()
        # Pi to 5 decimal places is 3.14159
        expected = 3.14159
        self.assertEqual(result, expected, 
                         f"Expected {expected}, but got {result}")
    
    def test_pi_is_float(self):
        """Test that the result is a float"""
        result = calculate_pi_to_5th_digit()
        self.assertIsInstance(result, float, 
                              "Result should be a float")
    
    def test_pi_is_positive(self):
        """Test that pi is positive"""
        result = calculate_pi_to_5th_digit()
        self.assertGreater(result, 0, 
                           "Pi should be positive")
    
    def test_pi_is_in_reasonable_range(self):
        """Test that pi is approximately 3.14"""
        result = calculate_pi_to_5th_digit()
        self.assertGreater(result, 3.1, 
                           "Pi should be greater than 3.1")
        self.assertLess(result, 3.2, 
                        "Pi should be less than 3.2")
    
    def test_pi_decimal_places(self):
        """Test that result has exactly 5 decimal places"""
        result = calculate_pi_to_5th_digit()
        # Round to 5 decimals and ensure it's equal (no extra precision)
        rounded = round(result, 5)
        self.assertEqual(result, rounded, 
                         "Result should be rounded to 5 decimal places")


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
