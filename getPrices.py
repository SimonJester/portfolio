#!/usr/bin/env python

"""
Retrieves current market prices for a list of cryptocurrencies 
via JSON from online.

To install BeautifulSoup, run one of these commands:
    apt-get install python-bs4
    easy_install beautifulsoup4
    pip install beautifulsoup4
Or, you can download the tarball and install it with:
    python setup.py install
"""

#TODO: Pass the 'prices' dictionary by reference into each get_prices_... function.
#TODO: Handle command line parms.
#TODO: As a last resort, if price cannot be determined then use the most recent price that we downloaded.
#TODO: Provide alternate methods of retrieving price info such as directly accessing the exchanges.

import sys
import urllib2
from bs4 import BeautifulSoup


def get_prices_from_coinmarketcap(prices=None):
    """
    Get current prices and their units of measure from coinmarketcap.
    This procedure returns a "prices" dictionary of this form:
        { ticker, [price, unit] }
            ticker and unit are unicode strings.
            price is float.
    This function modifies the dictionary in the caller's scope, 
    so it's equivalent to passing the 'prices' parameter by reference.
    """

    # If no prices passed in, then define the prices dictionary here
    if prices is None:
        prices = {}

    # Get all prices from the Internet in JSON format
    url = 'http://coinmarketcap.northpole.ro/api/all.json'
    web_response = urllib2.urlopen(url)
    json_data = json.loads(web_response.read())
    markets = json_data[u'markets']

    # Convert JSON market data into a dictionary
    EMPTY_VAL = u''
    for market in markets:
        prices[market[u'id']] = [float(market[u'price']), market[u'currency']]

    # Get list of non-market investments (no market price established yet)
    nm_investments = {
             u'eth': [0.0005, u'btc']
            ,u'zrc': [0.0, u'btc']
            ,u'swarm': [0.000194413, u'btc']
            }

    # Add non-market price info to the prices dictionary`
    for ticker in nm_investments:
        if ticker not in prices:
            prices[ticker] = nm_investments[ticker]

    return prices


def get_prices_from_kitco(prices=None):
    """
    Get current prices and their units of measure from kitco.
    This procedure returns a "prices" dictionary of this form:
        { ticker, [price, unit] }
            ticker and unit are unicode strings.
            price is float.
    This function modifies the dictionary in the caller's scope, 
    so it's equivalent to passing the 'prices' parameter by reference.
    """

    # If no prices passed in, then define the prices dictionary here
    if prices is None:
        prices = {}

    # Scrape web site for prices of gold, silver & platinum
    url = 'http://kitco.com'
    print "Please wait for Kitco site..."
    soup = BeautifulSoup(urllib2.urlopen(url).read())
    search_string = "Gold in USD"
    print soup.find_all(text=search_string)
    #print soup.find_all(text=search_string).contents[5]

    return prices


def get_prices():
    prices = {}  #Initialize empty dictionary
    #get_prices_from_coinmarketcap(prices)
    get_prices_from_kitco(prices)
    return prices


def main():
    """Parse command line options (TODO)"""
    print get_prices()


if __name__ == "__main__":
    main()

