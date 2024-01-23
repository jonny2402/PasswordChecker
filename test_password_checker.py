import unittest
from password_checker import PasswordStrengthChecker

class TestPasswordStrengthChecker(unittest.TestCase):
    def setUp(self):
        self.checker = PasswordStrengthChecker()

    def test_common_password(self):
        strength, feedback = self.checker.check_strength("password")
        self.assertEqual(strength, 'very weak')
        self.assertIn("Avoid common passwords.", feedback)

    def test_moderate_password(self):
        strength, _ = self.checker.check_strength("Abcd123")
        self.assertEqual(strength, 'moderate')

    def test_strong_password(self):
        strength, _ = self.checker.check_strength("Abc123$")
        self.assertEqual(strength, 'strong')

    def test_very_strong_password(self):
        strength, _ = self.checker.check_strength("A1b2C3$d")
        self.assertEqual(strength, 'very strong')
        
    def test_short_password(self):
        strength, feedback = self.checker.check_strength("Ab1$")
        self.assertEqual(strength, 'strong')
        self.assertIn("Use at least 8 characters.", feedback)

    def test_no_uppercase(self):
        _, feedback = self.checker.check_strength("abcd1234$")
        self.assertIn("Include both uppercase and lowercase letters.", feedback)

    def test_no_numbers(self):
        _, feedback = self.checker.check_strength("AbcdEFG$")
        self.assertIn("Include numbers.", feedback)

    def test_no_special_characters(self):
        _, feedback = self.checker.check_strength("AbcdEFG1")
        self.assertIn("Add special characters (e.g., @, #, $).", feedback)

if __name__ == "__main__":
    unittest.main()
