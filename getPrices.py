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

#TODO: Get a faster source of info, but use kitco as a backup (kitco takes 30 sec).
#TODO: Pass the 'prices' dictionary by reference into each get_prices_... function.
#TODO: Handle command line parms.
#TODO: As a last resort, if price cannot be determined then use the most recent price that we downloaded.
#TODO: Provide alternate methods of retrieving price info such as directly accessing the exchanges.

import sys
import urllib2
import json
import re


def get_prices_for_cryptocurrencies(prices=None):
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


def get_prices_for_metals(prices=None, url=None, regex=None):
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

    # Scrape web site for prices of gold, silver & platinum
    web_page = urllib2.urlopen(url).read()
    m = re.search(regex, web_page, re.DOTALL)
    #TODO: Handle exception for when no results are returned
    gold_price = float(m.group(1).replace(",",""))
    silver_price = float(m.group(2).replace(",",""))
    platinum_price = float(m.group(3).replace(",",""))
    print "Gold: ${}".format(gold_price)
    print "Silver: ${}".format(silver_price)
    print "Platinum: ${}".format(platinum_price)

    # Only enter the prices into the price dictionary that are missing
    #TODO...
    return prices


def get_prices():
    prices = {}

    #get_prices_for_cryptocurrencies(prices)

    get_prices_for_metals(
        prices,
        'http://money.cnn.com/data/commodities/', 
        'Metals.+?Gold.+?Electronic.+?([\d,]+\.\d+).+?Silver.+?Electronic.+?([\d,]+\.\d+).+?Platinum.+?Electronic.+?([\d,]+\.\d+)' 
        )

    # Use Kitco as backup in case CNN is not available
    get_prices_for_metals(
        prices,
        'http://kitco.com',
        'Gold in USD.+?([\d,]+\.\d+).+?kitcosilver\.com.+?([\d,]+\.\d+).+?liveplatinum\.html.+?([\d,]+\.\d+)' 
        )

    #get_prices_for_metals(
    #    prices,
    #    'http://bullion.nwtmint.com/spot-price-charts.php#tabs-2',
    #    'Gold.+?([\d,]+\.\d+).+?Silver.+?([\d,]+\.\d+).+?Platinum.+?([\d,]+\.\d+)'
    #    )

    #get_prices_for_metals(
    #    prices,
    #    'http://www.24hgold.com/english/home.aspx',
    #    'Gold.+?(\d+\.\d+).+?Silver.+?(\d+\.\d+).+?Platinum.+?(\d+\.\d+)'
    #    )

    return prices


def main():
    """Parse command line options (TODO)"""
    print get_prices()


if __name__ == "__main__":
    main()

