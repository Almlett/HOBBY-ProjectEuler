# Digit cancelling fractions
"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
import time

start_time = time.time()

def gcd(a, b):
    """
    Calculates the greatest common divisor (GCD) of two numbers 'a' and 'b' using Euclid's algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a

def cancel_digits(numerator, denominator):
    """
    Cancels a common digit between the numerator and denominator.
    Returns the simplified numerator and denominator as a tuple.
    """
    num_str = str(numerator)
    den_str = str(denominator)
    
    for digit in num_str:
        if digit in den_str:
            num_str = num_str.replace(digit, '', 1)
            den_str = den_str.replace(digit, '', 1)
            if den_str != '0':  # Avoid division by zero
                new_numerator = int(num_str)
                new_denominator = int(den_str)
                return new_numerator, new_denominator
    return numerator, denominator

def find_curious_fractions():
    curious_fractions = []
    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):  # Avoid trivial examples
            # Skip fractions that are multiples of 10 (trivial examples)
            if numerator % 10 == 0 and denominator % 10 == 0:
                continue
            
            simplified_numerator, simplified_denominator = cancel_digits(numerator, denominator)
            if simplified_numerator != numerator and simplified_denominator != denominator:
                if numerator / denominator == simplified_numerator / simplified_denominator:
                    curious_fractions.append((numerator, denominator))
    return curious_fractions

curious_fractions = find_curious_fractions()

# Calculate the product of the fractions in its lowest common terms
numerator_product = 1
denominator_product = 1

for fraction in curious_fractions:
    numerator_product *= fraction[0]
    denominator_product *= fraction[1]

# Find the greatest common divisor (GCD) of the numerator and denominator to simplify the fraction
gcd_value = gcd(numerator_product, denominator_product)
simplified_numerator = numerator_product // gcd_value
result = denominator_product // gcd_value

print("Result is:", result)
print("--- %s seconds ---" % (time.time() - start_time))

