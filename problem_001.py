#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Multiples of 3 and 5
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#Si enumeramos todos los números naturales por debajo de 10 que son múltiplos de 3 o 5, obtenemos 3, 5, 6 y 9. La suma de estos múltiplos es 23.
#Encuentra la suma de todos los múltiplos de 3 o 5 por debajo de 1000.


sum = 0
for num in range(1,1000):
    if num % 5 == 0 or num % 3 == 0:
        sum += num

print ("El resultado es : {}".format(sum))

# El resultado es :  233168
    