prices = [57.8, 46.51, 97, 199.99, 3.03, 79.07, 6, 99.99, 11, 0.99]
# A
print('Задача #A')
for cost in prices:
    rubles = int(cost)
    kopeks = round(cost * 100 % 100)
    print(f' «{rubles} руб {kopeks:02d} коп»', end=', ')
print('\n', prices, 'id списка:', id(prices))
# B
print('Задача #B')
prices.sort()
for cost in prices:
    rubles = int(cost)
    kopeks = round(cost * 100 % 100)
    print(f' «{rubles} руб {kopeks:02d} коп»', end=', ')
print('\n', prices, 'id списка:', id(prices))
# C
print('Задача #C')
new_prices = sorted(prices, reverse=True)
for cost in new_prices:
    rubles = int(cost)
    kopeks = round(cost * 100 % 100)
    print(f' «{rubles} руб {kopeks:02d} коп»', end=', ')
print('\n', new_prices, 'id списка:', id(new_prices))
# D
print('Задача #D')
for cost in sorted(new_prices[0:5], reverse=False):
    rubles = int(cost)
    kopeks = round(cost * 100 % 100)
    print(f' «{rubles} руб {kopeks:02d} коп»', end=', ')
print('\n', sorted(new_prices[0:5], reverse=False))
