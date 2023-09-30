import os
from pathlib import Path
from unittest import TestCase, skipIf

file_path = Path(__file__).absolute().parent / 'main.py'
is_file_empty = os.stat(file_path).st_size == 0

if not is_file_empty:
    from .main import days_in_a_month


@skipIf(is_file_empty, 'Empty file. Test 012 Skipped')
class TestDaysInAMonth(TestCase):


    def test_days_in_a_month_ok(self):
        """
        Test if return the correct value without a leap year
        """

        year = 2023

        months_and_result = {1: 31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

        for month, ok_result in months_and_result.items():
            result = days_in_a_month(month, year)
            self.assertEqual(ok_result, result, f'The days of the month numbered as {month} are {ok_result}')

    def test_days_in_a_month_leap_year_ok(self):
        """
        Test if return the correct value with a leap year
        """

        year = 2020

        months_and_result = {1: 31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

        for month, ok_result in months_and_result.items():
            result = days_in_a_month(month, year)
            self.assertEqual(ok_result, result)