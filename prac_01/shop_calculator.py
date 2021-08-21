item_prices = []  # List of item prices
DISCOUNT = .10  # 10% discount if price is over $100
num_items = int(input("Number of items: "))
while num_items <= 0:
    print("Must be more than 0")
    num_items = int(input("Number of items: "))
for i in range(0, num_items):
    price = float(input("Price of item: "))
    item_prices.append(price)
total = sum(item_prices)
if total > 100:
    discount = total * DISCOUNT
    new_price = total - discount
    print("Total price for {} items is ${:.2f}".format(num_items, new_price))
else:
    print("Total price for {} items is ${:.2f}".format(num_items, total))
