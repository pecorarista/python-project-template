# -*- coding: utf-8 -*-

import doctest
import unittest
import nyan.util as util


class TestUtil(unittest.TestCase):

    def test_duplicate(self):
        doctest.testmod(util, verbose=False)


if __name__ == '__main__':
    unittest.main()
