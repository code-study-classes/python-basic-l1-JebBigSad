prices = [1500, 6000, 4999, 12000, 800]

new_prices = [price * 0.8 if price > 5000 else price for price in prices]

print(f"Старые цены: {prices}")
print(f"Новые цены: {new_prices}")