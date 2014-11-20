#!/usr/bin/env python

"""
Prices all the ticker items passed to it.
"""

#TODO: Notify user when a USD ticker price cannot be determined.
#TODO: Print confirmation ('Done.') only if successful.
#TODO: Confirm that BTC prices were converted correctly to USD.
#TODO: Define EMPTY_VAL as #define in getTickers and import it to here.
#TODO: Handle command line parms.


from __future__ import print_function  #This *must* be the first line in the module.
import sys
import os
import csv
from getTickers import get_tickers
from getPrices import get_prices
from configPortfolio import portfolio_config_path as config_path
from configPortfolio import csv_filename_ticker_prices as result_filename


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
            print(" * Price not available for {}".format(ticker), 
                    file=sys.stderr)
            portfolio.append([ticker, EMPTY_VAL])

    return portfolio


def write_portfolio(portfolio, csv_filename=None):
    """
    Write the portfolio (with current prices) to a CSV file.
    If the the optional csv_filename parameter is omitted, 
    then the portfolio is written to a standard location.
    """
    if csv_filename is None:
        csv_filename = '{}/{}'.format(config_path, result_filename)
    with open(csv_filename, 'wb') as fp:
        writer = csv.writer(
                fp, 
                delimiter=',',
                quotechar='"', 
                quoting=csv.QUOTE_NONE)
        writer.writerows(portfolio)


def main():
    """Parse command line options (TODO)"""
    try:
        print('Getting ticker prices...', file=sys.stderr)
        my_tickers = get_tickers()
        my_portfolio = price_tickers(my_tickers)
        write_portfolio(my_portfolio)
        print('Done.', file=sys.stderr)
    except IOError:
        pass #Proper explanation is provided by the called functions


if __name__ == "__main__":
    main()

