# -*- coding: utf-8 -*-

from .context import fishws

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(fishws.hmm())


if __name__ == '__main__':
    unittest.main()
