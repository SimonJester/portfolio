#!/usr/bin/env python

import os

portfolio_config_path = '{}/.portfolio/'.format(os.getenv("HOME"))
csv_filename_tickers = 'tickers.csv'
csv_filename_ticker_prices = 'lastResult.csv'

#portfolio_config_path = ''
#csv_filename_tickers = ''
#csv_filename_ticker_prices = ''
#
#
#def main():
#    """Initialize global variables"""
#    portfolio_config_path = '{}/.portfolio/'.format(os.getenv("HOME"))
#    csv_filename_tickers = 'tickers.csv'
#    csv_filename_ticker_prices = 'lastResult.csv'
#
#
#if __name__ == '__main__':
#    main()
