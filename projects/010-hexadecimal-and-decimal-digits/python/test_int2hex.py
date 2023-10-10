from unittest import TestCase
from .main import int2hex

class TestInt2Hex(TestCase):

    def test_int2hex_ok(self):
        """
        test if function return the right value
        """

        int_and_hex = {
            1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
        }

        for integer, ok_result in int_and_hex.items():
            result = int2hex(integer)
            self.assertEqual(ok_result, result, f'Right hexadecimal number for {integer} is {ok_result}')
    

    def test_invalid_type(self):
        """
        Check if function correctly raise a ValueError if entered a value out of expected range
        """

        with self.assertRaises(ValueError):
            int2hex('45')
