#!/usr/bin/env python

"""
Prices all the ticker items passed to it.
"""

#TODO: Define EMPTY_VAL in getTickers and import it to here.
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
    portfolio = []

    # Price every ticker
    for index, ticker in enumerate(tickers):
        if ticker != EMPTY_VAL:
            if prices[ticker][1] == u'usd':
                # This is priced in USD, so copy
                #Copy ticker & price to portfolio
                portfolio.append([ticker, prices[ticker][0]])
            elif (prices[ticker][1] in prices 
                and prices[prices[ticker][1]][1] == u'usd'):
                # Not priced in USD *and* the conversion to USD does exist
                portfolio.append([ticker, 
                        prices[ticker][0] * prices[prices[ticker][1]][0]])

    return portfolio


def main():
    """Parse command line options (TODO)"""
    print price_tickers(get_tickers())


if __name__ == "__main__":
    main()

