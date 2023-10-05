import os
from pathlib import Path
from unittest import TestCase, skipIf

file_path = Path(__file__).absolute().parent / 'main.py'
is_file_empty = os.stat(file_path).st_size == 0

if not is_file_empty:
    from .main import integer_to_ordinal


@skipIf(is_file_empty, 'Empty file. Test 003 Skipped')
class TestIntegerToOrdinal(TestCase):

    def test_integer_to_ordinal_ok(self):
        """
        Check if return the correct result for number from 1 to 12
        """

        day_and_result = {1: 'first', 2:'second', 3:'third', 4:'fourth', 5:'fifth', 6:'sixth', 7:'seventh', 8:'eighth',
                          9:'ninth', 10:'tenth', 11:'eleventh', 12:'twelfth'}

        for day, ok_result in day_and_result.items():
            result = integer_to_ordinal(day).lower()
            self.assertEqual(ok_result, result, f'The ordinal of the integer {day} is {ok_result}')


    def test_integer_to_ordinal_outside_of_range(self):
        """
        Check if return an empty string if the function is called with an argument outside the range 1-12
        """

        result = integer_to_ordinal(15).lower()
        self.assertEqual('', result,
                         'Your function should return an empty string is called with an argument outside the range 1-12')

