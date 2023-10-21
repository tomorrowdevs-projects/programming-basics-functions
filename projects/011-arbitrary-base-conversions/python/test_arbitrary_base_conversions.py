import os
from pathlib import Path
from unittest import TestCase, skipIf

file_path = Path(__file__).absolute().parent / 'main.py'
is_file_empty = os.stat(file_path).st_size == 0

if not is_file_empty:
    from .main import arbitrary_to_base_10, base_10_to_arbitrary_base


@skipIf(is_file_empty, 'Empty file. Test 011 Skipped')
class TestArbitraryBaseConversions(TestCase):


    def test_arbitrary_to_base_10_base_2_ok(self):
        """
        Check if correctly converts from an arbitrary base (between 2 and 16) to base 10
        """

        base = 2
        numbers = list(range(0, base))

        for number in numbers:
            result = arbitrary_to_base_10(str(number), base)
            self.assertEqual(number, result,
                             f'The correct result for the number {number} with base {base} must be {number}')

    def test_arbitrary_to_base_10_base_3_ok(self):
        """
        Check if correctly converts from an arbitrary base (between 2 and 16) to base 10
        """

        base = 3
        numbers = list(range(0, base))

        for number in numbers:
            result = arbitrary_to_base_10(str(number), base)
            self.assertEqual(number, result,
                             f'The correct result for the number {number} with base {base} must be {number}')

    def test_arbitrary_to_base_10_base_4_ok(self):
        """
        Check if correctly converts from an arbitrary base (between 2 and 16) to base 10
        """

        base = 4
        numbers = list(range(0, base))

        for number in numbers:
            result = arbitrary_to_base_10(str(number), base)
            self.assertEqual(number, result,
                             f'The correct result for the number {number} with base {base} must be {number}')

    def test_arbitrary_to_base_10_base_5_ok(self):
        """
        Check if correctly converts from an arbitrary base (between 2 and 16) to base 10
        """

        base = 5
        numbers = list(range(0, base))

        for number in numbers:
            result = arbitrary_to_base_10(str(number), base)
            self.assertEqual(number, result,
                             f'The correct result for the number {number} with base {base} must be {number}')

    def test_arbitrary_to_base_10_base_6_ok(self):
        """
        Check if correctly converts from an arbitrary base (between 2 and 16) to base 10
        """

        base = 6
        numbers = list(range(0, base))

        for number in numbers:
            result = arbitrary_to_base_10(str(number), base)
            self.assertEqual(number, result,
                             f'The correct result for the number {number} with base {base} must be {number}')

    def test_arbitrary_to_base_10_base_7_ok(self):
        """
        Check if correctly converts from an arbitrary base (between 2 and 16) to base 10
        """

        base = 7
        numbers = list(range(0, base))

        for number in numbers:
            result = arbitrary_to_base_10(str(number), base)
            self.assertEqual(number, result,
                             f'The correct result for the number {number} with base {base} must be {number}')

    def test_arbitrary_to_base_10_base_8_ok(self):
        """
        Check if correctly converts from an arbitrary base (between 2 and 16) to base 10
        """

        base = 8
        numbers = list(range(0, base))

        for number in numbers:
            result = arbitrary_to_base_10(str(number), base)
            self.assertEqual(number, result,
                             f'The correct result for the number {number} with base {base} must be {number}')

    def test_arbitrary_to_base_10_base_9_ok(self):
        """
        Check if correctly converts from an arbitrary base (between 2 and 16) to base 10
        """

        base = 9
        numbers = list(range(0, base))

        for number in numbers:
            result = arbitrary_to_base_10(str(number), base)
            self.assertEqual(number, result,
                             f'The correct result for the number {number} with base {base} must be {number}')

    def test_arbitrary_to_base_10_base_10_ok(self):
        """
        Check if correctly converts from an arbitrary base (between 2 and 16) to base 10
        """

        base = 10
        numbers = list(range(0, base))

        for number in numbers:
            result = arbitrary_to_base_10(str(number), base)
            self.assertEqual(number, result,
                             f'The correct result for the number {number} with base {base} must be {number}')

    def test_arbitrary_to_base_10_base_11_ok(self):
        """
        Check if correctly converts from an arbitrary base (between 2 and 16) to base 10
        """

        base = 11
        numbers = list(range(0, base))

        ok_results = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]

        for number, ok_result in zip(numbers, ok_results):
            result = arbitrary_to_base_10(str(number), base)
            self.assertEqual(ok_result, result,
                             f'The correct result for the number {number} with base {base} must be {number}')

    def test_arbitrary_to_base_10_base_12_ok(self):
        """
        Check if correctly converts from an arbitrary base (between 2 and 16) to base 10
        """

        base = 12
        numbers = list(range(0, base))

        ok_results = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12]

        for number, ok_result in zip(numbers, ok_results):
            result = arbitrary_to_base_10(str(number), base)
            self.assertEqual(ok_result, result,
                             f'The correct result for the number {number} with base {base} must be {number}')


    def test_arbitrary_to_base_10_base_13_ok(self):
        """
        Check if correctly converts from an arbitrary base (between 2 and 16) to base 10
        """

        base = 13
        numbers = list(range(0, base))

        ok_results = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 13]

        for number, ok_result in zip(numbers, ok_results):
            result = arbitrary_to_base_10(str(number), base)
            self.assertEqual(ok_result, result,
                             f'The correct result for the number {number} with base {base} must be {number}')

    def test_arbitrary_to_base_10_base_14_ok(self):
        """
        Check if correctly converts from an arbitrary base (between 2 and 16) to base 10
        """

        base = 14
        numbers = list(range(0, base))

        ok_results = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 14]

        for number, ok_result in zip(numbers, ok_results):
            result = arbitrary_to_base_10(str(number), base)
            self.assertEqual(ok_result, result,
                             f'The correct result for the number {number} with base {base} must be {number}')

    def test_arbitrary_to_base_10_base_15_ok(self):
        """
        Check if correctly converts from an arbitrary base (between 2 and 16) to base 10
        """

        base = 15
        numbers = list(range(0, base))

        ok_results = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 15]

        for number, ok_result in zip(numbers, ok_results):
            result = arbitrary_to_base_10(str(number), base)
            self.assertEqual(ok_result, result,
                             f'The correct result for the number {number} with base {base} must be {number}')

    def test_arbitrary_to_base_10_base_16_ok(self):
        """
        Check if correctly converts from an arbitrary base (between 2 and 16) to base 10
        """

        base = 16
        numbers = list(range(0, base))

        ok_results = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 16]

        for number, ok_result in zip(numbers, ok_results):
            result = arbitrary_to_base_10(str(number), base)
            self.assertEqual(ok_result, result,
                             f'The correct result for the number {number} with base {base} must be {number}')



    # -------------------------------------------------------------------------------------------------------------- #
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
