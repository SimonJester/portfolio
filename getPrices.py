#!/usr/bin/env python

"""
Retrieves current prices for a list of cryptocurrencies via JSON from:
http://coinmarketcap.northpole.ro/api/all.json
"""

#TODO: Handle command line parms.

import sys
import json
import urllib2
from getPortfolio import get_portfolio


def get_prices(tickers):
    """Get current prices for all items in portfolio"""

    # Get all prices from the Internet in JSON format
    url = 'http://coinmarketcap.northpole.ro/api/all.json'
    web_response = urllib2.urlopen(url)
    json_data = json.loads(web_response.read())
    markets = json_data[u'markets']

    # Convert list into dictionary
    prices = [u''] * len(tickers)
    portfolio = dict(zip(tickers, prices))

    # Extract price info from JSON data
    for market in markets:
        if market[u'id'] in portfolio:
            portfolio[market[u'id']] = market[u'price']

    return portfolio


def main():
    """Parse command line options (TODO)"""
    print get_prices(get_portfolio())


if __name__ == "__main__":
    main()

