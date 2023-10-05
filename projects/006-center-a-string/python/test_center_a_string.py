import os
from pathlib import Path
from unittest import TestCase, skipIf

file_path = Path(__file__).absolute().parent / 'main.py'
is_file_empty = os.stat(file_path).st_size == 0

if not is_file_empty:
    from .main import center_string


@skipIf(is_file_empty, 'Empty file. Test 006 Skipped')
class TestCenterAString(TestCase):

    def test_string_greater_than_width_ok(self):
        """
        Check if return string if s > w
        """

        string_ = 'Embrace the journey, for within its twists and turns lies the beauty of discovery'
        width  = 10

        result = center_string(string_, width)
        self.assertEqual(string_, result)

    def test_string_equals_than_width_ok(self):
        """
        Check if return string if s = w
        """

        string_ = 'Embrace the journey, for within its twists and turns lies the beauty of discovery'
        width  = 10

        result = center_string(string_, width)
        self.assertEqual(string_, result)

    def test_string_less_than_width_ok(self):
        """
        Check if return (len(s) - w) // 2 if s < w
        """

        string_ = 'Embrace the journey, for within its twists and turns lies the beauty of discovery'
        width  = 100

        ok_result = '          Embrace the journey, for within its twists and turns lies the beauty of discovery'
        result = center_string(string_, width)
        self.assertEqual(ok_result, result)

