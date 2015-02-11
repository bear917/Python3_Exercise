import urllib.request

page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices.html")
text = page.read().decode("utf8")

# find the position of the price tag 
priceSearch = text.find(">$")
# after price tag, add offset 2
priceStart = priceSearch + 2
# price has 4 character 
priceEnd = priceStart + 4
price = text[priceStart:priceEnd]
print(price)
