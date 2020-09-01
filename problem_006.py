#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Sum square difference
# The sum of the squares of the first ten natural numbers is,
    # 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
    # (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


# La suma de los cuadrados de los primeros diez números naturales es,
    # 12 + 22 + ... + 102 = 385
# El cuadrado de la suma de los primeros diez números naturales es,
    # (1 + 2 + ... + 10) 2 = 552 = 3025
# Por lo tanto, la diferencia entre la suma de los cuadrados de los primeros diez números naturales y el cuadrado de la suma es 3025 - 385 = 2640.
# Encuentra la diferencia entre la suma de los cuadrados de los primeros cien números naturales y el cuadrado de la suma.


result = 0
sum = 0
mul = 0
for num in range(1,101):
    sum += num**2
    mul += num

mul = mul**2
result = mul - sum

print ("El resultado es : {}".format(result))

# El resultado es :  25164150
    