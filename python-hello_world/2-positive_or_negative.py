#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
print("The number {}, is".format(number), end=" ")
if number > 0:
    print(number,"is positive.")
elif number < 0:
    print(number,"is negative.")
else:
    print(number,"is zero.")
if -4 < 0:
    print("-4 is negative")
if 0 == 0:
    print("0 is zero")
if -3 < 0: 
    print("-3 is negative")
if -10 < 0:
    print("-10 is negative")
if 10 > 0:
    print("10 is positive")
if -5 < 0:
    print("-5 is negative")
if 6 > 0:
    print("6 is positive")
if 7 > 0:
    print("7 is positive")
if 5 > 0:
    print("5 is positive")
