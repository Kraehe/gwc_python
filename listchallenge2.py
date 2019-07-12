# This challenge is to make a random menu!

#imports the ability to get a random number
from random import *

#restaurant name
adjList = ["Dark", "Bright", "Funky", "Shady", "Peppy", "Fresh", "Spunky", "Orange", "Spotty"]
nList = ["Wolf", "Sphere", "Frog", "Gnome", "Deer", "Wizard", "Triangle", "Lizard", "Flame", "Snowflake", "Bead"]

#Generates a random integer that stays within the indices of the list
adjRandomIndex = randint(0, len(adjList)-1)
nRandomIndex = randint(0, len(nList)-1)

name = str(adjList[adjRandomIndex] + " " + nList[nRandomIndex])

#Lists of different sides, main courses, and desserts to choose from
sideList = ["fries", "mashed potatoes", "sweet potato fries", "popcorn", "rice", "beans", "salad"]
mainList = ["hangar steak", "burger", "veggie burger", "eggplant mozzarella", "chicken breast"]
dessertList = ["chocolate cake", "ice cream", "tiramisu", "cheesecake", "bread", "cupcakes"]


sides = []
for i in range(2):
    x = randint(0, len(sideList)-1)
    randSide = sideList[x]
    sides.append(randSide)


#Generates a random integer for the 2 different lists
bRandomIndex = randint(0, len(mainList)-1)
cRandomIndex = randint(0, len(dessertList)-1)


randMain = mainList[bRandomIndex]
randDess = dessertList[cRandomIndex]

print("Hello, welcome to the " + name + " restaurant!")
print("Today, our special consists of a main course of a " + randMain +  " with sides of " + sides[0] + " and " + sides[1]
+ ".\n If you have room for dessert, we also have "
+ randDess + ". Enjoy your meal!" )
