import os
from pathlib import Path
from unittest import TestCase, skipIf

file_path = Path(__file__).absolute().parent / 'main.py'
is_file_empty = os.stat(file_path).st_size == 0

if not is_file_empty:
    from .main import gregorian_to_ordinal_date


@skipIf(is_file_empty, 'Empty file. Test 005 Skipped')
class TestGregorianDateToOrdinalDate(TestCase):

    def test_gregorian_date_to_ordinal_date_no_leap_ok(self):
        """
        Check if return the correct with a no leap year
        """

        day = 19
        month = 8
        year = 2023

        ok_result = 231
        result = gregorian_to_ordinal_date(day, month, year)
        self.assertEqual(ok_result, result,
                         f'The ordinal date for the day: {day}, month: {month}, year: {year} '
                         f'must be {ok_result} and not your result: {result}')


    def test_gregorian_date_to_ordinal_date_leap_ok(self):
        """
        Check if return the correct with a leap year
        """

        day = 28
        month = 6
        year = 2020

        ok_result = 180
        result = gregorian_to_ordinal_date(day, month, year)
        self.assertEqual(ok_result, result,
                         f'The ordinal date for the day: {day}, month: {month}, year: {year} '
                         f'must be {ok_result} and not your result: {result}')
