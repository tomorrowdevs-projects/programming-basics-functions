import os
from pathlib import Path
from unittest import TestCase, skipIf

file_path = Path(__file__).absolute().parent / 'main.py'
is_file_empty = os.stat(file_path).st_size == 0

if not is_file_empty:
    from .main import arbitrary_to_base_10, base_10_to_arbitrary_base


@skipIf(is_file_empty, 'Empty file. Test 011 Skipped')
class TestArbitraryBaseConversions(TestCase):


    def test_arbitrary_to_base_10_ok(self):
        """
        Check if correctly converts from an arbitrary base (between 2 and 16) to base 10
        """

        for base in range(2, 17):
            numbers = list(range(0, base))

            for number in numbers:
                result = arbitrary_to_base_10(str(number), base)
                self.assertEqual(int(number), result,
                                 f'The correct result for the number {number} with base {base} must be {number}')


    def test_base_10_to_arbitrary_base_ok(self):
        """
        Check if correctly converts from base 10 to an arbitrary base (between 2 and 16)
        """

        number = 50
        base_ok_result = {2:'110010', 3:'1212', 4:'302', 5:'200', 6:'122', 7:'101', 8:'62',
                          9:'55', 10:'50', 11:'46', 12:'42', 13:'3B', 14:'38', 15:'35', 16:'32'}


        for base, ok_result in base_ok_result.items():
            result = base_10_to_arbitrary_base(number, base)
            self.assertEqual(ok_result, result,
                             f'The correct result for the number {number} with base {base} must be {ok_result}')
