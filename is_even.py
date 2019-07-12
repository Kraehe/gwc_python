from random import *

num = randint(1,100)

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(num)
print(is_even(num))
