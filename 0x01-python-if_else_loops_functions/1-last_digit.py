#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
newNum = repr(number)[-1]
if int(newNum) > 5:
    print(f"Last digit of {number} is {newNum} and is greater than 5")
elif int(newNum) == 0:
    print(f"Last digit of {number} is {newNum} and is 0")
else:
    if int(newNum) < 6 and not 0:
        print(f"Last digit of {number} is {newNum} and is less than 6 and not 0")
