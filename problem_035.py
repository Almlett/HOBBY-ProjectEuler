"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
import time

start_time = time.time()

result = 0

def is_prime(num):
    """
    Checks if a given number 'num' is prime.
    """
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:  # Even numbers
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):  # Odd numbers
        if num % i == 0:
            return False
    return True

def get_combinations(num):
    """
    Generates all possible combinattions of the digits of a given number 'num'.
    """
    num_str = str(num)
    for i in range(len(num_str)):
        yield int(num_str[i:] + num_str[:i])
            
def count_circular_primes(limit):
    """
    Counts the number of circular primes below the given 'limit'.
    """
    circular_primes = set()
    for num in range(2, limit):
        if all(is_prime(rotated_num) for rotated_num in get_combinations(num)):
            circular_primes.add(num)
            yield num


result = len(list(count_circular_primes(1000000)))
print("Result is:", result)
print("--- %s seconds ---" % (time.time() - start_time))
# 55
