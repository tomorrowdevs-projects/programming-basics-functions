import os
from pathlib import Path
from unittest import TestCase, skipIf

file_path = Path(__file__).absolute().parent / 'main.py'
is_file_empty = os.stat(file_path).st_size == 0

if not is_file_empty:
    from .main import reduce_measures


@skipIf(is_file_empty, 'Empty file. Test 013 Skipped')
class TestReduceMeasures(TestCase):

    def test_reduce_measures_teaspoon_ok(self):
        """
        Check if return the correct result with teaspoon as unit of measure
        """

        unit_of_measure = 'teaspoon'

        result = reduce_measures(50, unit_of_measure)
        self.assertIn('1 cup, 0 tablespoon, 2 teaspoons', result)

        result = reduce_measures(14, unit_of_measure)
        self.assertIn('0 cup, 4 tablespoons, 2 teaspoons', result)

        result = reduce_measures(1, unit_of_measure)
        self.assertIn('0 cup, 0 tablespoon, 1 teaspoon', result)

    def test_reduce_measures_tablespoon_ok(self):
        """
        Check if return the correct result with tablespoon as unit of measure
        """

        unit_of_measure = 'tablespoon'

        result = reduce_measures(35, unit_of_measure)
        self.assertIn('2 cups, 3 tablespoons, 0 teaspoon', result)

        result = reduce_measures(73, unit_of_measure)
        self.assertIn('4 cups, 4 tablespoons, 0 teaspoon', result)

        result = reduce_measures(1, unit_of_measure)
        self.assertIn('0 cup, 1 tablespoons, 0 teaspoon', result)

    def test_reduce_measures_cup_ok(self):
        """
        Check if return the correct result with cup as unit of measure
        """

        unit_of_measure = 'cup'

        result = reduce_measures(35, unit_of_measure)
        self.assertIn('35 cups, 0 tablespoon, 0 teaspoon', result)
