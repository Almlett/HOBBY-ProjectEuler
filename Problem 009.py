#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Special Pythagorean triplet
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#    a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.


# Un triplete pitagórico es un conjunto de tres números naturales, a <b <c, para el cual,
#   a2 + b2 = c2
#Por ejemplo,   32 + 42 = 52 
#               9 + 16 = 25
# Existe exactamente un triplete de Pitágoras para el que a + b + c = 1000.
#Encuentra el producto abc.


result = 0 
for a in range(1,1001):
    for b in range(1,1001):
        for c in range(1,1001):
            if a + b + c == 1000:
                if a**2 + b**2 == c**2:
                    print ("El resultado es : {} * {} * {} = {}".format(a,b,c,a*b*c))



# El resultado es :  31875000
    