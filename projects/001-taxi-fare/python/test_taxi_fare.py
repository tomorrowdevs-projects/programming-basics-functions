import os
from pathlib import Path
from unittest import TestCase, skipIf

file_path = Path(__file__).absolute().parent / 'main.py'
is_file_empty = os.stat(file_path).st_size == 0

if not is_file_empty:
    from .main import taxi_fare


@skipIf(is_file_empty, 'Empty file. Test 001 Skipped')
class TestTaxiFare(TestCase):


    def test_taxi_fear_plus_ok(self):
        """
        Test if return the correct value with a plus
        """

        distance = 20


        try:
            # get only 2 decimal position
            result = round(taxi_fare(distance), 2)
            self.assertEqual(39.71, result, 'Value different that the expected')

        except TypeError:
            print(f' > The value returned from your function is not a float type.\n')
            assert False

    def test_taxi_fear_no_plus_ok(self):
        """
        Test if return the correct value without a plus
        """

        distance = 0

        try:
            # get only 2 decimal position
            result = round(taxi_fare(distance), 2)
            self.assertEqual(4.0, result, 'Value different that the expected')

        except TypeError:
            print(f' > The value returned from your function is not a float type.\n')
            raise False

