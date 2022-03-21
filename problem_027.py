# Quadratic primes
"""
Euler discovered the remarkable quadratic formula:

...
"""
import time
start_time = time.time()


def is_prime(num):
    prime = True
    for inside_num in range(2, num):
        if num % inside_num == 0:
            prime = False
            break
    return prime


def formula(n, a, b):
    # n2 + an +b
    return (n ** 2) + (a * n) + b


def get_quantity(a, b):
    n = 0
    if is_prime(abs(a)) and is_prime(abs(b)):
        while True:
            if is_prime(abs(formula(n, a, b))):
                n += 1
            else:
                break
    return n


_a = 0
_b = 0
_quantity = 0
_product = 0

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        quantity = get_quantity(a, b)
        if quantity > _quantity:
            _a = a
            _b = b
            _quantity = quantity

print("{} primes when \n\ta: {}, \n\tb: {}, \n\tproduct: {} \nin {} seconds".format(
    _quantity, _a, _b, _a * _b, (time.time() - start_time)))


#print(get_quantity(-79, 1601))
#print(get_quantity(1, 41))
#print(get_quantity(-61, 971), -61*971)
