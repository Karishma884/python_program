#
fruit_prices = {
    'apple': 50,
    'banana': 20,
    'orange': 30
}
grape_price = fruit_prices.get('grape', 'Price not found')
print("The price of grape is:", grape_price)