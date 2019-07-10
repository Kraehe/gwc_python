import random

# A list of words
potential_words = ["example", "words", "someone", "can", "guess"]

word = random.choice(potential_words)

# Use to test your code:
print(word)

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
current_word = []
letters = list(word)
print(len(letters))
for i in range(len(letters)):
    current_word.append("_")
print(current_word)
 # TIP: the number of letters should match the word

# Some useful variables
guesses = []
maxfails = 7
fails = 0
guess = ""
while fails < maxfails:
    print(guesses)
    guess = input("Guess a letter: ")
    if guess in letters:
        print("You got a letter!")
        for letter in # loop through the word and check where the guess is equal to the letter in the word!! continue looking l8r
        guesses.append(guess)
    else:
        print("you didn't get a letter ):")
# check if the guess is valid: Is it one letter? Have they already guessed it?

# check if the guess is correct: Is it in the word? If so, reveal the letters!
#
    print(current_word)
#
    fails = fails+1
    print("You have " + str(maxfails - fails) + " tries left!")
