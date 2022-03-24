# Coin sums
"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
import time
from tkinter import E
start_time = time.time()


combinations = []

coins = [200, 100, 50, 20, 10, 5, 2, 1]
combinations = []


def get_combinations(_coins, limit):
    for coin in coins:
        if sum(_coins) + coin < limit:
            return get_combinations(_coins + [coin], limit)
        elif sum(_coins) + coin == limit:
            return _coins + [coin]
        elif sum(_coins) == limit:
            return _coins
        else:
            pass


_all = []
for coin in coins:
    tmp_combination = []
    for _coin in coins:
        tmp = get_combinations([_coin], coin)
        if tmp:
            tmp_combination.append(tmp)
    combinations.append({'coin': coin, 'combinations': len(tmp_combination)})
    _all.append(tmp_combination)


print(_all)
print("--- %s seconds ---" % (time.time() - start_time))
# 73682
