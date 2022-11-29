#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    l_n = ((number * -1) % 10) * -1
else:
    l_n = number % 10
if l_n > 5:
    print(f"Last digit of {number:d} is {l_n:d} and is greater than 5")
elif l_n == 0:
    print(f"Last digit of {number:d} is {l_n:d} and is 0")
elif l_n < 6 and not 0:
    print(f"Last digit of {number:d} is {l_n:d} and is less than 6 and not 0")
