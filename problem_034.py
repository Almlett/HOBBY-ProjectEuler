# Digit factorials
"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""


def get_factorial(num):
    if num == 1 or num == 2:
        return num

    result = 1
    for i in range(1, num+1):
        result *= i
    return result


def isdigit_factorial(num):
    str_num = str(num)
    result = 0
    for item in str_num:
        result += get_factorial(int(item))
    return result == num


for i in range(10, 1000000):
    if isdigit_factorial(i):
        print(i)
