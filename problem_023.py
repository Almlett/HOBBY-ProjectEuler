#Non-abundant sums
"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import time


def get_divisors(num):
    for i in range(1, num):
        if num % i == 0:
            yield i
    

def is_abundant(num):
    return sum(get_divisors(num)) > num

#def abundant_nums():
#    for i in range(12,28124):
#        if is_abundant(i):
#            yield i

abundant_nums = [num for num in range(12,28124) if is_abundant(num)]    

def get_abundant_sums():
    result = []
    for x in abundant_nums:
        for y in abundant_nums:
            if x + y <= 28123:
                result.append(x + y)
    print("TERMINO1")
    return result

def get_not_abundants_nums():
    abundant_sums = get_abundant_sums()
    for num in range(28124):
        if num not in abundant_sums:
            yield num

start_time=time.time()


print(sum(get_not_abundants_nums()))
print("--- %s seconds ---" % (time.time() - start_time))
#TIME: 628.0386536121368 seconds
#RESULT: 4179871