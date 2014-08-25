#!/usr/bin/env python

"""
Retrieves current list of ticker symbols that are in portfolio.
All symbols are in lower-case.
"""

#TODO: Get portfolio list from a csv file that I created from my original spreadsheet.
#TODO: Handle command line parms.

import sys
from __future__ import print_function


def get_tickers():
    """Return a list of ticker symbols for entire portfolio"""
    # Currently this list is hardcoded to match my spreadsheet layout
    portfolio = [
             u'BTC'
            ,u'LTC'
            ,u'ETH'
            ,u''
            ,u''
            ,u'ZRC'
            ,u'NMC'
            ,u'MSC'
            ,u'ANC'
            ,u'NXT'
            ,u'XCP'
            ,u''
            ,u''
            ,u'PTS'
            ,u'BTSX'
            ,u''
            ,u''
            ,u'XPM'
            ,u'PPC'
            ,u'FTC'
            ,u'SWARM'
            ,u'DRK'
            ,u'MAID'
            ,u'TOR'
            ,u''
            ,u''
            ,u'DOGE'
            ,u'MEC'
            ,u'QRK'
            ,u'XRP'
            ,u'SJCX'
            ]

    # Convert to lowercase
    return [ticker.lower() for ticker in portfolio]


def main():
    """Parse command line options (TODO)"""
    print(get_tickers())


if __name__ == "__main__":
    main()

