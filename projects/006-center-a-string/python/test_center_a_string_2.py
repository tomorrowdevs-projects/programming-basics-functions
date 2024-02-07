import unittest

from main import center_string

class Test_center_a_string(unittest.TestCase):

    def test_center_a_string_one(self):
        '''Check that the function returns the correct result when the inserted string is longer than the screen'''

        result = center_string('This screen is smaller then the string', 5)
        self.assertEqual(result,'This screen is smaller then the string')


    def test_center_a_string_two(self):
        '''Check that the function returns the correct result when the inserted string has an equal length of the screen'''

        result = center_string('This screen is equal then the string',36)
        self.assertEqual(result,'This screen is equal then the string')


    def test_center_a_string_three(self):
        '''Check that the function returns the correct result when the inserted string has a smaller screen length'''

        result = center_string('    This screen is larger then the string    ', 44)
        self.assertEqual(result,'    This screen is larger then the string    ')


if __name__ == '__main__': 
    unittest.main()      