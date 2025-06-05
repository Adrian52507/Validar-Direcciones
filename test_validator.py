import unittest
from validator import is_valid_address

class TestValidator(unittest.TestCase):
    def test_valid_address(self):
        self.assertTrue(is_valid_address("Av. Siempre Viva 742"))
    def test_missing_number(self):
        self.assertFalse(is_valid_address("Av. Siempre Viva"))
    def test_empty_string(self):
        self.assertFalse(is_valid_address(""))
    def test_not_a_string(self):
        self.assertFalse(is_valid_address(12345))
    
if __name__ == "__main__":
    unittest.main()