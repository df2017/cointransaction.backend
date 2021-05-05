import requests
from bs4 import BeautifulSoup

def price_market_coins():
    url = "https://coinmarketcap.com/es/"

    html =  requests.get(url)
    soup = BeautifulSoup(html.content, "lxml")
    currencies = ["bitcoin", "ethereum", "xrp", "tether", "litecoin", "dai"]
    currencies_prices_list = []

    for currency in currencies:
        find_currency = "/es/currencies/{}/markets/".format(currency)
        find_amount = soup.find("a", {'href': find_currency})
        if find_amount:
            currencies_prices_list.append({currency: find_amount.text.replace("$","")})
        else:
            currencies_prices_list.append({currency: find_amount})
    print(currencies_prices_list)
    return currencies_prices_list

price_market_coins()