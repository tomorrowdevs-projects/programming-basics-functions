import os
from pathlib import Path
from unittest import TestCase, skipIf

file_path = Path(__file__).absolute().parent / 'main.py'
is_file_empty = os.stat(file_path).st_size == 0

if not is_file_empty:
    from .main import is_valid_password


@skipIf(is_file_empty, 'Empty file. Test 009 Skipped')
class TestPasswordValidation(TestCase):


    def test_password_validation_ok(self):
        """
        Check if correctly validate the password
        """

        password = 'SecureP@ssword123'

        result = is_valid_password(password)
        self.assertTrue(result)

    def test_password_validation_len_false(self):
        """
        Check if correctly validate the password shorter than 8
        """

        password = 'Secur1'

        result = is_valid_password(password)
        self.assertFalse(result)

    def test_password_validation_uppercase_false(self):
        """
        Check if correctly validate the password without uppercase
        """

        password = 'securep@ssword123'

        result = is_valid_password(password)
        self.assertFalse(result)

    def test_password_validation_lowercase_false(self):
        """
        Check if correctly validate the password without lowercase
        """

        password = 'SECUREP@SSWORD123'

        result = is_valid_password(password)
        self.assertFalse(result)

    def test_password_validation_number_false(self):
        """
        Check if correctly validate the password without numbers
        """

        password = 'SecureP@ssword'

        result = is_valid_password(password)
        self.assertFalse(result)



