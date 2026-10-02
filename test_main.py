import unittest

from main import (
    check_length,
    has_lowercase,
    has_uppercase,
    has_number,
    has_special_character,
    is_common_password,
    has_repeated_characters,
    has_sequential_pattern,
    get_length_score
)

class TestPasswordChecks(unittest.TestCase):

    def test_length(self):
        self.assertTrue(check_length("abcdefgh"))
        self.assertFalse(check_length("abc"))

    def test_lowercase(self):
        self.assertTrue(has_lowercase("abc"))
        self.assertFalse(has_lowercase("ABC123"))

    def test_uppercase(self):
        self.assertTrue(has_uppercase("ABC"))
        self.assertFalse(has_uppercase("abc123"))

    def test_number(self):
        self.assertTrue(has_number("abc123"))
        self.assertFalse(has_number("abcdef"))

    def test_special_character(self):
        self.assertTrue(has_special_character("abc!"))
        self.assertFalse(has_special_character("abc123"))

    def test_common_password(self):
        self.assertTrue(is_common_password("password"))
        self.assertTrue(is_common_password("Password123"))
        self.assertFalse(is_common_password("BlueTiger42!")) 

    def test_repeated_characters(self):
        self.assertTrue(has_repeated_characters("aaa"))
        self.assertTrue(has_repeated_characters("abc111xyz"))
        self.assertFalse(has_repeated_characters("abcdef"))

    def test_sequential_pattern(self):
        self.assertTrue(has_sequential_pattern("hello1234"))
        self.assertTrue(has_sequential_pattern("abcdef"))
        self.assertFalse(has_sequential_pattern("BlueTiger42!"))

    def test_length_score(self):
        self.assertEqual(get_length_score("abc"), 0)
        self.assertEqual(get_length_score("abcdefgh"), 1)
        self.assertEqual(get_length_score("abcdefghijkl"), 2)
        self.assertEqual(get_length_score("abcdefghijklmnop"), 3)


if __name__ == "__main__":
    unittest.main()