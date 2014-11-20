#!/usr/bin/env python

"""
Retrieves current list of ticker symbols that are in portfolio.

Input text should not have spaces or quotes around strings 
because those characters will also become part of the ticker name.
If a comma appears in any text, then only the text prior to the 
comma will be used.

All symbols returned are in lower-case Unicode.
"""

#TODO: Handle command line parms.

from __future__ import print_function
import sys
import os
import csv
from configPortfolio import portfolio_config_path as config_path
from configPortfolio import csv_filename_tickers as tickers_filename


def read_tickers(csv_filename):
    """Read ticker symbols from first column of a csv file"""
    portfolio = []
    with open(csv_filename, 'rb') as fp:
        reader = csv.reader(
                fp, 
                delimiter=',', 
                quoting=csv.QUOTE_NONE)
        for row in reader:
            try:
                portfolio.append(unicode(row[0]))
            except IndexError:  #Handle empty rows
                portfolio.append(u'')
        fp.close()
    return portfolio


def write_tickers(portfolio, csv_filename):
    """Write ticker symbols to a one-column csv file"""
    with open(csv_filename, 'wb') as fp:
        writer = csv.writer(
                fp, 
                delimiter=',', 
                quoting=csv.QUOTE_NONE)
        for ticker in portfolio:
            writer.writerow([ticker]) #Must make ticker a list to avoid commas
        fp.close()


def get_tickers(csv_filename=None):
    """Return a list of ticker symbols for entire portfolio"""
    if csv_filename is None:
        #TODO: Deteremine if the HOME env variable is ever *not* defined.
        #TODO: Test on Windows.
        csv_filename = '{}/{}'.format(config_path, tickers_filename)
    try:
        portfolio = read_tickers(csv_filename)
    except IOError:
        print("*** Error: Tickers File is Missing.", file=sys.stderr)
        print("      Create a csv file and save it as {}".format(csv_filename), 
                file=sys.stderr)
        print("      It should contain one column of text containing ticker symbols without any commas.", 
                file=sys.stderr)
        raise
    else:
        return [ticker.lower() for ticker in portfolio]


def main():
    """Parse command line options (TODO)"""
    print(get_tickers())


if __name__ == "__main__":
    main()

