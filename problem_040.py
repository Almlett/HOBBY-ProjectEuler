"""
An irrational decimal fraction is created by concatenating the positive integers:

    0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1. 

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d100000 x d100000 x d1000000
"""
import time

start_time = time.time()

def generate_champernowne_constant(to):
    """
    Generates the Champernowne Constant up to the given position 'to'.
    """
    result = "0."
    for index in range(1, to + 1):
        result += str(index)
    return result

def get_digit_at_position(data, position):
    """
    Returns the digit at the given position after the decimal point in the Champernowne Constant.
    """
    items = data.split(".")[1]
    return int(items[position - 1])

data = generate_champernowne_constant(1000000)

request = [1, 10, 100, 1000, 10000, 100000, 1000000]
result = 1
for item in request:
    result *= get_digit_at_position(data, item)

print(result)
print("--- %s seconds ---" % (time.time() - start_time))
# 210
