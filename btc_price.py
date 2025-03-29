from bs4 import BeautifulSoup
import requests
from datetime import datetime

yahoo_finance_site = requests.get("https://coinmarketcap.com/currencies/bitcoin/").text
soup = BeautifulSoup(yahoo_finance_site, "html.parser")
btc_price = soup.find("span", {"class": "sc-65e7f566-0 WXGwg base-text"})

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
price_text = btc_price.text if btc_price else "Price not found"
log_line = f"{timestamp}, {price_text}\n"

with open("btc_prices.csv", "a") as file:
    file.write(log_line)
