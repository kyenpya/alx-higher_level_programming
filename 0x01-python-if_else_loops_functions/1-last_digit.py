#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastNum = number % (-10)
else:
    lastNum = number % 10

if number > 5:
    print(f"Last digit of {number} is {lastNum} and is greater than 5")
elif number == 0:
    print(f"Last digit of {number} is {lastNum} and is 0")
elif number < 6 and number != 0:
    print(f"Last digit of {number} is {lastNum} and is less than 6 and not 0")
