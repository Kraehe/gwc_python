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
dessertList = ["chocolate cake", "ice cream", "tiramisu", "cheesecake", "bread", "cupcake"]

#Generates a random integer for the 3 different lists
aRandomIndex = randint(0, len(sideList)-1)
bRandomIndex = randint(0, len(mainList)-1)
cRandomIndex = randint(0, len(dessertList)-1)

randSide = sideList[aRandomIndex]
randMain = mainList[bRandomIndex]
randDess = dessertList[cRandomIndex]

print("Hello, welcome to the " + name + " restaurant!")
print("Today, our special consists of a main course of a " + randMain +  " with a side of " + randSide
+ ", and if you have room for dessert, we also have "
+ randDess + ". We hope you enjoy your meal!" )
