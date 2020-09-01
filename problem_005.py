#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Smallest multiple
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# 2520 es el número más pequeño que se puede dividir por cada uno de los números del 1 al 10 sin ningún resto.
# ¿Cuál es el número positivo más pequeño que es divisible por todos los números del 1 al 20?


result = 0
num = 1
verify = False
while(True):
    verify = True
    for inside_num in range(1,21):
        if num % inside_num != 0:
            verify = False
            break
    if verify:
        result = num
        break
    num += 1

print ("El resultado es : {}".format(result))

# El resultado es :  232792560
    