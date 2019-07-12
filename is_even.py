from random import * # imports the random library

num = randint(5,3000) # sets a variable equal to a random number between 1 and 100

def is_even(num): # defines our function that takes in a number
    if num % 2 == 0: # checks if the remainder of the number is 0 when divided by 2
        return True  # returns true if even
    else:
        return False
print(num)
print(is_even(num))
