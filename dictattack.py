#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")

print("Can your password survive a dictionary attack?")

def pwd():
    #Take input from the keyboard, storing in the variable test_password
    #NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
    test_password = input("Type in a trial password:\n>> ").strip().lower()
    #Write logic to see if the password is in the dictionary file below here:

    # Checks the length of the password
    if len(test_password) < 8:
        print("Your password is too short!")
        pwd()
    # Initializes the 'words' variable
    words = 0
    isaword = False
    pwords = []
    # Loops through each line in the dictionary
    for line in f:
        # Checks if the password is a word in the dictionary
        if test_password == line.strip():

            isaword = True

        elif line.strip()in test_password and len(line.strip()) >= 3:
                words += 1
                pwords.append(line.strip())
        else:

            continue

    if isaword == True:
        print("Your password, ", test_password, " did not survive, it was too weak!!")
    if words > 0:
        print("Your password has ", words, " words in it!")


    for word in pwords:
        print(word, " found in password!")

pwd()
