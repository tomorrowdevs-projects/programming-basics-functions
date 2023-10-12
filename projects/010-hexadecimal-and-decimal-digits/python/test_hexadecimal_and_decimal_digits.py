import os
from pathlib import Path
from unittest import TestCase, skipIf

file_path = Path(__file__).absolute().parent / 'main.py'
is_file_empty = os.stat(file_path).st_size == 0

if not is_file_empty:
    from .main import hex2int, int2hex


@skipIf(is_file_empty, 'Empty file. Test 010 Skipped')
class TestHexadecimalAndDecimalDigits(TestCase):


    def test_hex2int_ok(self):
        """
        Check if correctly convert a string containing a single hexadecimal digit to a base 10 integer.
        """

        hexa_ok_result = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
                                 '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

        for hexa, ok_result  in hexa_ok_result.items():
            result = hex2int(hexa)
            self.assertEqual(ok_result, result, f'The correct decimal for the hexa {hexa} must be {ok_result}')


    def test_int2hex_ok(self):
        """
        Check if correctly convert an integer between 0 and 15 into is hexadecimal digit
        """

        number_ok_result = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
                            9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

        for number, ok_result  in number_ok_result.items():
            result = str(int2hex(number))
            self.assertEqual(ok_result, result,
                             f'The correct hexadecimal for the number {number} must be {ok_result}')


