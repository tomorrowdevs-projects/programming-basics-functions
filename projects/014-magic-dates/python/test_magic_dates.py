import os
from pathlib import Path
from unittest import TestCase, skipIf

file_path = Path(__file__).absolute().parent / 'main.py'
is_file_empty = os.stat(file_path).st_size == 0

if not is_file_empty:
    from .main import is_magic_date


@skipIf(is_file_empty, 'Empty file. Test 014 Skipped')
class TestMagicDates(TestCase):

    def test_is_magic_date_true_ok(self):
        """
        Check if correctly return True with a magic date
        """

        result = is_magic_date(1, 1, 1901)
        self.assertTrue(result)

        result = is_magic_date(27, 2, 1954)
        self.assertTrue(result)

        result = is_magic_date(24, 4, 1996)
        self.assertTrue(result)

    def test_is_magic_date_false_ok(self):
        """
        Check if correctly return False with a no magic date
        """

        result = is_magic_date(4, 10, 1993)
        self.assertFalse(result)

        result = is_magic_date(2, 4, 1954)
        self.assertFalse(result)

        result = is_magic_date(17, 9, 1996)
        self.assertFalse(result)




