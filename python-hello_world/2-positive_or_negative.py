#!/usr/bin/python3
import random
number = random.randint(-99, 99)
# YOUR CODE HERE
print("The number {}, is".format(number), end=" ")
if number > 0:
    print(number,"is positive.")
elif number < 0:
    print(number,"is negative.")
else:
    print(number,"is zero.")
