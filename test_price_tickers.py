#!/usr/bin/env python

import pytest
from priceTickers import price_tickers


def test_price_tickers():
    """Test happy path for pricing of tickers."""
    actual = price_tickers('data_get_tickers_unix_input.csv')
    expected = read_tickers('data_get_tickers_expected.csv')
    assert actual == expected


def main():
    test_price_tickers()


if __name__ == '__main__':
    main()

