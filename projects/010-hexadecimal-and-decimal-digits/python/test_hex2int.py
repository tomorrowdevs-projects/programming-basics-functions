from unittest import TestCase
from .main import hex2int

class TestHex2Int(TestCase):

    def test_if_hex2int_ok(self):
        """
        test if function return the right result
        """

        hex_numbers = {
            '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
        }

        for hexadecimal, ok_result in hex_numbers.items():
            result = hex2int(hexadecimal.upper())
            self.assertEqual(ok_result, result, f'Int number of hex {hexadecimal} is {ok_result}')

        
    def test_lowercase(self):
        """
        check if a lowercase letter work properly in function
        """

        result = hex2int('a')
        self.assertEqual(result, 10, 'Function should work with upper and lowercase equally.')


    def test_uppercase(self):
        """
        check if a uppercase letter work properly in function
        """

        result = hex2int('A')
        self.assertEqual(result, 10, 'Function should work with upper and lowercase equally.')


    def test_invalid_value(self):
        """
        Check if function correctly raise a ValueError if entered a value out of expected range
        """

        with self.assertRaises(ValueError):
            hex2int('G')
    
    