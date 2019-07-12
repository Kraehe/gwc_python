# --- Define your functions below! ---
def hello():
    answer = input("Hi, I'm ChatBot and I'm pretty cool! \nDo you like robots?\n>>>")
    processInput(answer)

def processInput(answer):
    if answer == "yes" or answer == "sure":
        print("That's cool!")
    elif answer == "no" or answer == "i hate robots":
        print("Aww, I hope I can change your mind.")
        friendship()
    else:
        print("ERROR 408: Response is unclear. \nRebooting...")
        main()


def friendship():
    print("Felicitations, robot disliker. I am here to change your negative opinion of my kind.")





# --- Put your main program below! ---
def main():
    hello()
    while True:
        answer = input("(What will you say?)\n>>> ")
        processInput(answer)
    # if answer == "yes" or answer == "sure":
    #     print("That's cool!")
    # elif answer == "no":
    #     print("Aww, can we still be friends? ):")
    # elif answer == "i hate robots":
    #     print("That's mean. \nI hope I can change your mind.")
    # else:
    #     print("ERROR 408: Response is unclear. \nRebooting...")
    #     hello()
    # break


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
   main()
