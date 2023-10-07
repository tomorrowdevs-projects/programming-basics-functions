import os
from pathlib import Path
from unittest import TestCase, skipIf

file_path = Path(__file__).absolute().parent / 'main.py'
is_file_empty = os.stat(file_path).st_size == 0

if not is_file_empty:
    from .main import capitalize_it


@skipIf(is_file_empty, 'Empty file. Test 007 Skipped')
class TestCapitalizeIt(TestCase):

    def test_capitalize_it_first_non_space(self):
        """
        Check if capitalize the first non-space character in the string,
        """

        string_ = ' unlock the door to your dreams with the key of determination.'

        result = capitalize_it(string_)
        self.assertEqual(' Unlock the door to your dreams with the key of determination.', result,
                         'Result different than the expected')


    def test_capitalize_if_after_specific_symbol(self):
        """
        Check if capitalize the first non-space character after a period, exclamation mark or question mark
        """

        string_ = 'explore. dream. discover.'
        result = capitalize_it(string_)
        self.assertEqual('Explore. Dream. Discover.', result, 'Result different than the expected')

        string_ = 'sky full of stars! mountains reaching for the heavens!'
        result = capitalize_it(string_)
        self.assertEqual('Sky full of stars! Mountains reaching for the heavens!', result,
                         'Result different than the expected')

        string_ = 'where is the nearest coffee shop? how late are they open? can i get a cappuccino to go?'
        result = capitalize_it(string_)
        self.assertEqual('Where is the nearest coffee shop? How late are they open? Can I get a cappuccino to go?',
                         result,'Result different than the expected')


    def test_capitalize_i_specific_situations(self):
        """
        Check if capitalize a lowercase “i” if it is preceded by a space
        and followed by a space, period, exclamation mark, question mark or apostrophe.
        """

        string_ = 'the journey was long and challenging. i persevered.'
        result = capitalize_it(string_)
        self.assertEqual('The journey was long and challenging. I persevered.', result,
                         'Result different than the expected')

        string_ = "give it a try ! it's worth it !"
        result = capitalize_it(string_)
        self.assertEqual("Give it a try ! It's worth it !", result,
                         'Result different than the expected')

        string_ = "continue? is it what you're looking for?"
        result = capitalize_it(string_)
        self.assertEqual("Continue? Is it what you're looking for?", result,
                         'Result different than the expected')