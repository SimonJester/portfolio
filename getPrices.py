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

Note: I used regexpal.com to hone the regular expression.
"""

#TODO: If price cannot be determined then use the most recent price that we downloaded.
#TODO: Use kitco as a backup source for metals prices (kitco takes 30 sec).
#TODO: Provide alternate methods of retrieving price info such as directly accessing the exchanges.
#TODO: Have a backup source for crypto prices.
#TODO: Pass the 'prices' dictionary by reference into each get_prices_... function.
#TODO: Convert EMPTY_VAL into a #define

import sys
import urllib2
import json
import re


def get_prices_for_cryptocurrencies(prices=None):
    """
    Get current prices and their units of measure from online.
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
        ticker = market[u'id'] 
        if ticker not in prices:  #Only save if it hasn't been saved yet
            prices[ticker] = [float(market[u'price']), market[u'currency']]

    return prices


def get_non_market_prices_for_cryptocurrencies(prices=None):
    """
    Get current prices and their units of measure from a list defined by me.
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

    # Get list of non-market investments (no market price established yet)
    #TODO: Get this info from a text file
    nm_investments = {
             u'eth': [0.0005, u'btc']
            ,u'zrc': [0.0, u'btc']
            ,u'swarm': [0.000194413, u'btc']
            }

    # Add non-market price info to the prices dictionary
    for ticker in nm_investments:
        if ticker not in prices:
            prices[ticker] = nm_investments[ticker]

    return prices


def get_prices_for_metals(prices=None, url=None, regex=None, metals_sequence=None):
    """
    Get current prices and their units of measure from the chosen website.
    This procedure returns a "prices" dictionary of this form:
        { ticker, [price, unit] }
            ticker and unit are unicode strings.
            price is float.
    This function modifies the dictionary in the caller's scope, 
    so it's equivalent to passing the 'prices' parameter by reference.
    """

    # If no parms passed in, then define the defaults
    if prices is None:
        prices = {}
    if url is None:
        url = 'http://money.cnn.com/data/commodities/'
    if regex is None:
        regex = 'Metals.+?Gold.+?Electronic.+?([\d,]+\.\d+).+?Silver.+?Electronic.+?([\d,]+\.\d+).+?Platinum.+?Electronic.+?([\d,]+\.\d+)' 
    if metals_sequence is None:
        # Define the order-of-occurrence of prices in regex
        metals_sequence = [u'gold', u'silver', u'platinum']  

    # Scrape web site for metals prices
    web_page = urllib2.urlopen(url).read()
    #TODO: Handle exception for when the URL is bad
    matches = re.search(regex, web_page, re.DOTALL)
    #TODO: Handle exception for when no results are returned
    #TODO: Make it so partial matches still succeed for some prices
    
    # Enter the prices into the price dictionary
    for index, metal in enumerate(metals_sequence):
        prices[metal] = [float(matches.group(index).replace(",","")), u'usd']

    return prices


def get_prices():
    """
    Get prices for cryptocurrencies and metals and store them in one dictionary
    called "prices".
    """
    prices = {}

    #get_prices_for_cryptocurrencies(prices)

    get_prices_for_metals(
        prices,
        'http://money.cnn.com/data/commodities/', 
        'Metals.+?Gold.+?Electronic.+?([\d,]+\.\d+).+?Silver.+?Electronic.+?([\d,]+\.\d+).+?Platinum.+?Electronic.+?([\d,]+\.\d+)',
        [u'gold', u'silver', u'platinum']
        )

    # Use Kitco as backup in case CNN is not available
    get_prices_for_metals(
        prices,
        'http://kitco.com',
        'Gold in USD.+?([\d,]+\.\d+).+?kitcosilver\.com.+?([\d,]+\.\d+).+?liveplatinum\.html.+?([\d,]+\.\d+)',
        [u'gold', u'silver', u'platinum']
        )

    #get_prices_for_metals(
    #    prices,
    #    'http://bullion.nwtmint.com/spot-price-charts.php#tabs-2',
    #    'Gold.+?([\d,]+\.\d+).+?Silver.+?([\d,]+\.\d+).+?Platinum.+?([\d,]+\.\d+)',
    #    [u'gold', u'silver', u'platinum']
    #    )

    #get_prices_for_metals(
    #    prices,
    #    'http://www.24hgold.com/english/home.aspx',
    #    'Gold.+?(\d+\.\d+).+?Silver.+?(\d+\.\d+).+?Platinum.+?(\d+\.\d+)',
    #    [u'gold', u'silver', u'platinum']
    #    )

    return prices


def main():
    """Parse command line options (TODO)"""
    print get_prices()


if __name__ == "__main__":
    main()

