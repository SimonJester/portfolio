#!/usr/bin/env python

"""
Retrieves current list of ticker symbols that are in portfolio.
All symbols are in lower-case.
"""

#TODO: Get portfolio list from a text file.
#TODO: Handle command line parms.

import sys


def get_portfolio():
    """Return a list of ticker symbols for entire portfolio"""
    # Currently this list is hardcoded to match my spreadsheet layout
    portfolio = [
         'BTC'
        ,'LTC'
        ,'ETH'
        ,''
        ,''
        ,'ZRC'
        ,'NMC'
        ,'MSC'
        ,'ANC'
        ,'NXT'
        ,'XCP'
        ,''
        ,''
        ,'PTS'
        ,'BTSX'
        ,''
        ,''
        ,'XPM'
        ,'PPC'
        ,'FTC'
        ,'SWARMPRE'
        ,'DRK'
        ,'MAID'
        ,'TOR'
        ,''
        ,''
        ,'DOGE'
        ,'MEC'
        ,'QRK'
        ,'XRP'
        ]

    # Convert to lowercase
    return [ticker.lower() for ticker in portfolio]


def main():
    """Parse command line options (TODO)"""
    print get_portfolio()


if __name__ == "__main__":
    main()

