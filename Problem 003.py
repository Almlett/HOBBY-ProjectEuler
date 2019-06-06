#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Los factores primos de 13195 son 5, 7, 13 y 29.
# ¿Cuál es el mayor factor primo del número 600851475143?


max_prime = 0
max_num = 600851475143
if max_num % 2 == 0:
    lastFactor = 2 
    max_num = max_num / 2
    while (max_num % 2 == 0):
        max_num = max_num / 2
else:
    lastFactor = 1
factor = 3
maxFactor = max_num
while ( max_num > 1 and factor <= maxFactor):
    if max_num % factor == 0:
        max_num = max_num / factor
        lastFactor = factor
        while (max_num % factor == 0 ):
            max_num= max_num / factor
        maxFactor = max_num  
    factor = factor + 2
if max_num == 1:
    max_prime = lastFactor 
else:
    max_prime = max_num


print ("El resultado es : {}".format(max_prime))

#El resultado es : 6857