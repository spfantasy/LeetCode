# -*- coding: utf-8 -*-

import unittest
from ddt import ddt, data, unpack

from solution import *


@ddt
class TestXorGreaterCount(unittest.TestCase):
    @data(
        ([1, 2, 3, 4, 5, 6, 7], 7, 0),
        ([1, 2, 3, 4, 5, 6, 7], 6, 3),
        ([1, 2, 3, 4, 5, 6, 7], 5, 6),
        ([1, 2, 3, 4, 5, 6, 7], 4, 9),
        ([1, 2, 3, 4, 5, 6, 7], 3, 12),
        ([1, 2, 3, 4, 5, 6, 7], 2, 15),
        ([1, 2, 3, 4, 5, 6, 7], 1, 18),
        ([1, 2, 3, 4, 5, 6, 7], 0, 21),
        ([2, 3, 5, 7, 11, 13, 17, 19], 11, 16),
        ([2, 3, 5, 7, 11, 13, 17, 19], 8, 18),
        # [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]
        ([], 0, 0),
    )
    @unpack
    def test_xor_greater_count(self, nums, m, result):
        self.assertEqual(
            result, Solution().xor_greater_than(nums, m))


if __name__ == '__main__':
    unittest.main(verbosity=1)
