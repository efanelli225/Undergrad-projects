# -*- coding: utf-8 -*-
"""
Title: Code Assignment 1
Author: Eva Fanelli
Date: 08/24/2026
"""
import numpy as np

##############
# Problem 1
##############
# sums the numbers 1 through 137, including 1 and excluding 137. 

x=0
for i in range(137):
    x += i
print(x)

##############
# Problem 2
##############
# determines if a year x is a leap year

x = 3086
if x%4==0:
    print(f'{x} is a leap year')
else: 
    print(f'{x} is not a leap year')

##############
# Problem 3
##############
# counts the number of digits in a number x

x = 983125
y = x
count = 0
while x > 1 :
    x /= 10
    count += 1
print(f'{y} has {count} digits.')
    
##############
# Problem 4
##############
# determines if a number from 1 to 100 is divisible by 3, 5, both, or none

numbers = np.arange(1, 101)

for num in numbers:
    if num%3==0:
        if num%5==0:
            print(f'{num} FizzBuzz')
        else: 
            print(f'{num} Fizz')
    elif num%5==0:
        print(f'{num} Buzz')









