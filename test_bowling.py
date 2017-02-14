from unittest import TestCase

from bowling import get_total_score


class BowlingTestCase(TestCase):
    def test_all_strikes(self):
        point_list = [10]*12
        self.assertEqual(300, get_total_score(point_list))

    def test_all_ones(self):
        point_list = [1] * 20
        self.assertEqual(20, get_total_score(point_list))

    def test_all_zeroes(self):
        point_list = [0] * 20
        self.assertEqual(0, get_total_score(point_list))

    def test_get_total_score(self):
        point_list = [10, 3, 7, 6, 1, 10, 10, 10, 2, 8, 9, 0, 7, 3, 10, 10, 10]
        self.assertEqual(193, get_total_score(point_list))
