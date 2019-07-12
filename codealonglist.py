# basically listchallenge2.py but done differently and in class
# gets the stuff we need to generate random #s
from random import *

#lists of foods
side = ["food yum", "yummy food yes", "mmmm food", "yummy yummy"]
main = ["BIG YUM", "delicious main dish", "pizza yes", "good eats"]
desserts = ["pies", "ice cream", "cupcakes", "cake", "flan", "miserable fruits. you should feel bad."]

# empty list initialized to hold 2 side values
sideList = []

# loops through sides twice and puts values in sideList
for i in range(2):
    x = randint(0, len(side)-1)
    randSide = side[x]
    sideList.append(randSide)

# checks if both randomly selected sides are the same, and if they are just print one instead of both
if sideList[0] in sideList[1]:
    print("side: " + sideList[0])
else:
    print("sides: " + sideList[0] + " and " + sideList[1])


# selects a random main dish
randMainIndex = randint(0, len(main)-1)
randMain = main[randMainIndex]
print("main dish: " + randMain)

# selects a random dessert
randDessertIndex = randint(0, len(desserts)-1)
randDessert = desserts[randDessertIndex]
print("desserts: " + randDessert)
