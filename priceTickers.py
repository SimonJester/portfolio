#!/usr/bin/env python

"""
Prices all the ticker items passed to it.
"""

#TODO: Notify user when a USD ticker price cannot be determined.
#TODO: Print confirmation ('Done.') only if successful.
#TODO: Confirm that BTC prices were converted correctly to USD.
#TODO: Define EMPTY_VAL as #define in getTickers and import it to here.
#TODO: Handle command line parms.


import sys
import csv
from getTickers import get_tickers
from getPrices import get_prices


def price_tickers(tickers):
    """
    Return a portfolio, which is a list of this format:
        [ [ticker1, price1], [ticker2, price2], ... ]
    All prices are in USD and floating point.
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
        #TODO: Handle case where ticker does not exist in prices.
        #TODO: When conversion unit is not available is it graceful?
        try:
            if ticker == EMPTY_VAL:
                portfolio.append([EMPTY_VAL, EMPTY_VAL])
            elif prices[ticker][1] == u'usd':
                # This is priced in USD, so copy ticker & price to portfolio
                portfolio.append([ticker, prices[ticker][0]])
            elif (prices[ticker][1] in prices 
                and prices[prices[ticker][1]][1] == u'usd'):
                # Not priced in USD *and* the conversion to USD does exist
                portfolio.append([ticker, 
                        prices[ticker][0] * prices[prices[ticker][1]][0]])
        except KeyError:
            print "Price not available for {}".format(ticker)
            portfolio.append([EMPTY_VAL, EMPTY_VAL])

    return portfolio


def write_portfolio(portfolio, csv_filename):
    with open(csv_filename, 'wb') as fp:
        writer = csv.writer(
                fp, 
                delimiter=',',
                quotechar='"', 
                quoting=csv.QUOTE_NONE)
        writer.writerows(portfolio)


def main():
    """Parse command line options (TODO)"""
    write_portfolio(price_tickers(get_tickers()), 'forSpreadsheet.csv')
    print 'Done.'


if __name__ == "__main__":
    main()

