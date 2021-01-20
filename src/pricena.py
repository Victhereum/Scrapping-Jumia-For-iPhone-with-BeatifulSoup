import requests
from bs4 import BeautifulSoup

#<span dir="ltr" data-price="520999">520,999</span>

request = requests.get("https://www.jumia.com.ng/iphone-xs-max-4gb-ram-512gb-rom-ios-12-12mp-12mp7mp-space-gray-dual-sim-nano-sim-apple-mpg234854.html")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class": "price"})
string_price = element.text.strip() #520,999
price_without_symbol = string_price[1:]
string_price_without_comma = price_without_symbol.replace(',', '')
price = int(string_price_without_comma)
print(price)

if price < 500000:
    print("It just dropped to 500000")
    print("the price is now {}".format(string_price))
elif price > 500000:
    print("The price is still high")
    print("the price is {}".format(string_price))


