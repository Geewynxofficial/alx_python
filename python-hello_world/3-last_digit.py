#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_digit = abs(number) % 10
last_digit_number = -last_digit if number < 0 else last_digit

print(f"Last digit of {number} is {last_digit_number} and is", end=" ")

if last_digit_number > 5:
    print("greater than 5")
elif last_digit_number == 0:
    print("is 0")
elif last_digit_number < 6:
    print("less than 6 and not 0")
