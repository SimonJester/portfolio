#!/usr/bin/env python

import unittest
import getTickers

class TestGetTickers(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_tickers(self):
        tickers = getTickers('test_get_tickers_input.csv')
        expected = readTickers('test_get_tickers_expected.csv')
        for ticker in tickers:
            
            self.assert???()


if __name__ == '__main__':
    unittest.main()

