#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Un número palindrómico se lee igual en ambos sentidos. El palíndromo más grande hecho del producto de dos números de 2 dígitos es 9009 = 91 × 99.
# Encuentre el palíndromo más grande hecho del producto de dos números de 3 dígitos.


max = 0
val = 0
for first_num in range(1,1000):
    for second_num in range(1,1000):
        val = first_num * second_num
        val_string = str(val)
        if val_string[:len(val_string)/2] == val_string[len(val_string)/2:][::-1]:
            if val > max:
                max = val

print ("El resultado es : {}".format(max))

# El resultado es : 906609
    