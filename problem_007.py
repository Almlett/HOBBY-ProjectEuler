#!/usr/bin/env python
# -*- coding: utf-8 -*-

#10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


# Al enumerar los primeros seis números primos: 2, 3, 5, 7, 11 y 13, podemos ver que el sexto primo es 13.
# ¿Cuál es el número primo 10 001st?


position = 0
val_search = 10001
num = 1
while(position < 10001):
    num += 1
    
    #print("\n\n\n" + str(num) + "\n")
    prime = True
    for inside_num in range(2,num):
        #print("{} - {}".format(inside_num,num % inside_num))
        if num % inside_num == 0:
            prime = False
            break
    
    if prime:
        position += 1
        if position == val_search:
            print ("El resultado es : {}".format(num))
            break
   

# El resultado es :  104743
    