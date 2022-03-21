# Digit fifth powers
"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
import time
start_time = time.time()


def digit_powers(num, power):
    total = 0
    for i in str(num):
        total = total + (int(i) ** power)
    return num == total


def get_list(power):
    limit_down = int("1"+(power-1)*"0")
    limit_up = int("1"+(power)*"0")
    for num in range(limit_down, limit_up):
        if digit_powers(num, power):
            yield num


print(sum(get_list(5)))

print("--- %s seconds ---" % (time.time() - start_time))
# 443839
