#!/usr/bin/env python

"""
Retrieves current prices for a list of cryptocurrencies via JSON from:
http://coinmarketcap.northpole.ro/api/all.json
"""

#TODO: Get portfolio list from a text file.
#TODO: Handle command line parms.

import sys


def get_portfolio():
    """Return a list of ticker symbols for entire portfolio"""
    # Currently this list is hardcoded to match my spreadsheet layout
    return [
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


def get_current_prices(portfolio):
    """Get current prices for all items in portfolio"""
    # Get ALL prices from the Internet in one call

    prices = []
    for ticker in portfolio:

    return prices


def main():
    """Parse command line options (TODO)"""
    print get_portfolio()


if __name__ == "__main__":
    main()

