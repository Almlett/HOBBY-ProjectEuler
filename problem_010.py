#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Summation of primes
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

# La suma de los números primos debajo de 10 es 2 + 3 + 5 + 7 = 17.
#Encuentra la suma de todos los números primos por debajo de dos millones.


position = 0
result = 0
num = 1

def isPrime(num):
    prime = True
    for inside_num in range(2,num):
        #print("{} - {}".format(inside_num,num % inside_num))
        if num % inside_num == 0:
            prime = False
            break
    return prime    

while(position < 10001):
    num += 1
    prime = True
    for inside_num in range(2,num):
        #print("{} - {}".format(inside_num,num % inside_num))
        if num % inside_num == 0:
            prime = False
            break
    if prime:
        result += num
    if num == 2000000:
        break

print ("El resultado es : {}".format(result))


# El resultado es :  142913828922
    