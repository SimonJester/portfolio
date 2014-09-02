#!/usr/bin/env python

import pytest
#TODO: Determine what tempfile is used for.
#import tempfile
from getTickers import get_tickers
from getTickers import read_tickers

#TODO: Determine what the following three lines are for.
#import logging
#logging.basicConfig(level=logging.DEBUG, format='%(message)s')
#logger = logging.getLogger()


def test_get_tickers_unix():
    """Test various types of inputs with unix line endings"""
    actual = get_tickers('data_get_tickers_unix_input.csv')
    expected = read_tickers('data_get_tickers_expected.csv')
    assert actual == expected

def test_get_tickers_win():
    """Test Windows line endings"""
    actual = get_tickers('data_get_tickers_win_input.csv')
    expected = read_tickers('data_get_tickers_expected.csv')
    assert actual == expected

def test_get_tickers_mac():
    """Test Mac line endings"""
    actual = get_tickers('data_get_tickers_mac_input.csv')
    expected = read_tickers('data_get_tickers_expected.csv')
    assert actual == expected

def test_get_tickers_unicode():
    """Test Unicode characters"""
    actual = get_tickers('data_get_tickers_unicode_input.csv')
    expected = read_tickers('data_get_tickers_expected.csv')
    assert actual == expected

def test_get_tickers_empty_file():
    """Test empty file file"""
    expected = []
    actual = get_tickers('data_read_tickers_empty_file_input.csv')
    assert actual == expected


def main():
    test_get_tickers_unix()
    test_get_tickers_win()
    test_get_tickers_mac()
    test_get_tickers_unicode()
    test_get_tickers_empty_file()


if __name__ == '__main__':
    main()

