#!/usr/bin/env python

"""
Prices all the ticker items passed to it.
"""

#TODO: Handle command line parms.

import sys
import json
import urllib2
from getTickers import get_tickers
from getPrices import get_prices



def price_tickers(tickers):
    """
    Return a portfolio, which is a list of this format:
        [ [ticker, price], ... ]
    All prices will be in USD.
    This procedure retains the original sort order of the tickers and
    will not touch any blank items so as to retain spacing needed for 
    spreadsheet layout, so this info can be copied and pasted into a 
    spreadsheet.
    """

    # Initialize
    prices = get_prices()  #Dictionary of prices
    EMPTY_VAL = u''
    portfolio = [[0.0, EMPTY_VAL]] * len(tickers)

    # Price every ticker
    for index, ticker in enumerate(tickers):
        if ticker == EMTPY_VAL:
            # This is a blank spot used for spreadsheet layout, skip it
            continue
        elif prices[ticker][1] = u'usd':
            # This is priced in USD, so copy
            portfolio[index][0] = ticker  #Copy ticker
            portfolio[index][PRICE] = prices[ticker][0]  #Copy price

    return portfolio


def main():
    """Parse command line options (TODO)"""
    print price_tickers(get_tickers())


if __name__ == "__main__":
    main()

