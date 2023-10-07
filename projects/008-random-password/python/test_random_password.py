import os
from pathlib import Path
from unittest import TestCase, skipIf

file_path = Path(__file__).absolute().parent / 'main.py'
is_file_empty = os.stat(file_path).st_size == 0

if not is_file_empty:
    from .main import random_password


@skipIf(is_file_empty, 'Empty file. Test 008 Skipped')
class TestRandomPassword(TestCase):

    def test_random_password_len_ok(self):
        """
        Check if the length is between 7 and 10 characters
        """

        result = random_password()
        self.assertTrue(7 <= len(result) <= 10, 'The len of the password must be between 7 and 10.')


    def test_random_password_characters_ok(self):
        """
        Check if each character is randomly selected from positions 33 to 126 in the ASCII table.
        """

        ok_ascii = [chr(i) for i in range(33, 127)]
        result = random_password()

        for character in result:
            self.assertIn(character, ok_ascii,
                          f'Character {character} is not included in the list of ASCII from 33 to 126')


