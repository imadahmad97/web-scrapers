from bs4 import BeautifulSoup
import requests

yahoo_finance_site = requests.get("https://coinmarketcap.com/currencies/bitcoin/").text

soup = BeautifulSoup(yahoo_finance_site, "html.parser")

btc_price = soup.find("span", {"class": "sc-65e7f566-0 WXGwg base-text"})
print(btc_price.text)
