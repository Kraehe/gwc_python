# This challenge is to generate random names!

#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
adjList = ["Dark", "Bright", "Funky", "Shady", "Peppy", "Fresh", "Spunky", "Orange", "Spotty"]
nList = ["Wolf", "Sphere", "Frog", "Gnome", "Deer", "Wizard", "Triangle", "Lizard", "Flame", "Snowflake", "Bead"]

#Generates a random integer that stays within the indices of the list
aRandomIndex = randint(0, len(adjList)-1)
bRandomIndex = randint(0, len(nList)-1)

print(adjList[aRandomIndex] + " " + nList[bRandomIndex])
