# Digit factorials
"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""
import time

start_time = time.time()

def get_factorial(num):
    """
    Calculates the factorial of a given number 'num'.
    """
    if num == 1 or num == 2:
        return num

    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def is_digit_factorial(num):
    """
    Checks if the sum of the factorials of the digits of 'num' equals 'num'.
    """
    str_num = str(num)
    result = 0
    for item in str_num:
        result += get_factorial(int(item))
    return result == num

result = 0
for i in range(10, 1000000):
    if is_digit_factorial(i):
        result += i

print("Result is:", result)
print("--- %s seconds ---" % (time.time() - start_time))
# 40730
