# Pandigital products
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
import time
from unicodedata import numeric
start_time = time.time()


def is_pandigital(numbers):
    result = []
    for item in numbers:
        for digit in str(item):
            result.append(digit)
    return set(result) == set('123456789')


multiplos = []
multiplos = [39, 186]
multiplos.append(multiplos[0] * multiplos[1])


result = 0
for i in range(10, 100):
    multiplos = []
    second_num = 1
    while(True):
        if(len(str(i*second_num)) == 4):
            if is_pandigital([i, second_num, i * second_num]):
                result += i * second_num
                print(i, second_num, i * second_num)
                break
        elif(len(str(i*second_num)) > 4):
            break
        second_num += 1


print(result)
print("--- %s seconds ---" % (time.time() - start_time))
# 45228
