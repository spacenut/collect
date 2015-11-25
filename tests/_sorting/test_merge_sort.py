import unittest
from base_sort import SortTestMixin
import sorting


class TestMergeSort(unittest.TestCase):
    """Test sorting method. """

    sort_test = SortTestMixin('merge sort', sorting.merge_sort)

    def test_empty(self):
        type(self).sort_test._test_empty(self)

    def test_singleton(self):
        type(self).sort_test._test_singleton(self)

    def test_small(self):
        type(self).sort_test._test_small(self)

    def test_big(self):
        type(self).sort_test._test_big(self)