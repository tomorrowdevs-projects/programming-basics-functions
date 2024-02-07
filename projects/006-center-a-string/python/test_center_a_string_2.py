import unittest

from main import center_string

class Test_center_a_string(unittest.TestCase):

    def test_center_a_string_one(self):
        '''Check whether it returns the string correctly when the inserted string is larger than the screen'''

        result = center_string('This screen is smaller then the string', 5)
        self.assertEqual(result,'This screen is smaller then the string')


    def test_center_a_string_two(self):
        '''Check whether it returns the string correctly when the inserted string is larger than the screen'''
        
        result = center_string('This screen is equal then the string',36)
        self.assertEqual(result,'This screen is equal then the string')


    def test_center_a_string_three(self):
        '''Check whether it returns the string correctly when the inserted string is larger than the screen'''

        result = center_string('    This screen is larger then the string    ', 44)
        self.assertEqual(result,'    This screen is larger then the string    ')


if __name__ == '__main__': 
    unittest.main()      