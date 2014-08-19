#!/usr/bin/env python

"""
Retrieves current market prices for a list of cryptocurrencies 
via JSON from online.
"""

#TODO: Handle command line parms.
#TODO: As a last resort, if price cannot be determined then use the most recent price that we downloaded.
#TODO: Provide alternate methods of retrieving price info such as directly accessing the exchanges.

import sys
import json
import urllib2


def get_prices():
    """
    Get current prices and their units of measure.
    This procedure returns a "prices" dictionary of this form:
        { ticker, [price, unit] }
            ticker and unit are unicode strings.
            price is float.
    """

    # Get all prices from the Internet in JSON format
    url = 'http://coinmarketcap.northpole.ro/api/all.json'
    web_response = urllib2.urlopen(url)
    json_data = json.loads(web_response.read())
    markets = json_data[u'markets']

    # Convert JSON market data into a dictionary
    prices = {}
    EMPTY_VAL = u''
    for market in markets:
        prices[market[u'id']] = [float(market[u'price']), market[u'currency']]

    # Get list of non-market investments (no market price established yet)
    nm_investments = {
             u'eth': [0.0005, u'btc']
            ,u'zrc': [0.0, u'btc']
            ,u'swarmpre': [0.000194413, u'btc']
            }

    # Add non-market price info to the prices dictionary`
    for ticker in nm_investments:
        if ticker not in prices:
            prices[ticker] = nm_investments[ticker]

    return prices


def main():
    """Parse command line options (TODO)"""
    print get_prices()


if __name__ == "__main__":
    main()

