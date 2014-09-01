#!/usr/bin/env python

"""
Retrieves current list of ticker symbols that are in portfolio.
Input text must *not* have spaces or quotes around strings.

All symbols returned are in lower-case Unicode.
"""

#TODO: Handle command line parms.

import sys
import os
import csv


def read_tickers(csv_filename):
    """Read ticker symbols from first column of a csv file"""
    portfolio = []
    with open(csv_filename, 'rb') as fp:
        reader = csv.reader(
                fp, 
                delimiter=',', 
                quotechar='"', 
                quoting=csv.QUOTE_NONE)
        for row in reader:
            try:
                #TODO: Convert to Unicode if needed
                portfolio.append(row[0])
            except IndexError:  #Handle empty rows
                portfolio.append(u'')
        fp.close()
    return portfolio


def write_tickers(portfolio, csv_filename):
    """Write ticker symbols to a one-column csv file"""
    #TODO: Handle empty string for csv_filename.
    with open(csv_filename, 'wb') as fp:
        writer = csv.writer(
                fp, 
                delimiter=',', 
                quotechar='"', 
                quoting=csv.QUOTE_NONE)
        for ticker in portfolio:
            writer.writerow([ticker]) #Must make ticker a list to avoid commas
        fp.close()


def get_tickers(csv_filename=None):
    """Return a list of ticker symbols for entire portfolio"""
    if csv_filename is None:
        #TODO: Deteremine if the HOME env variable is ever *not* defined.
        csv_filename = '{}/.portfolio/tickers.csv'.format(os.getenv("HOME"))
    portfolio = read_tickers(csv_filename)
    # Convert to lowercase
    return [ticker.lower() for ticker in portfolio]


def main():
    """Parse command line options (TODO)"""
    print get_tickers()


if __name__ == "__main__":
    main()

