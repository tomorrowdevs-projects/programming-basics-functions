import os
from pathlib import Path
from unittest import TestCase, skipIf

file_path = Path(__file__).absolute().parent / 'main.py'
is_file_empty = os.stat(file_path).st_size == 0

if not is_file_empty:
    from .main import shipping_calculator


@skipIf(is_file_empty, 'Empty file. Test 002 Skipped')
class TestShippingCalculator(TestCase):

    def test_shipping_calculator_one_item_ok(self):
        """
        Check if return the correct value with one item
        """

        number_of_items = 1

        try:
            # get only 2 decimal position
            result = round(shipping_calculator(number_of_items), 2)
            self.assertEqual(10.99, result, 'Value different that the expected')

        except TypeError as error:
            print(f' > The value returned from your function is not a float type.\n', error)


    def test_shipping_calculator_more_items_ok(self):
        """
        Check if return the correct value with more items
        """

        number_of_items = 48

        try:
            # get only 2 decimal position
            result = round(shipping_calculator(number_of_items), 2)
            self.assertEqual(151.52, result, 'Value different that the expected')

        except TypeError as error:
            print(f' > The value returned from your function is not a float type.\n', error)


