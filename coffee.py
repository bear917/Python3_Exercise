import urllib.request

page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices.html")
text = page.read().decode("utf8")


priceSearch = text.find(">$")
priceStart = priceSearch + 2
priceEnd = priceStart + 4
price = text[priceStart:priceEnd]
print(price)
