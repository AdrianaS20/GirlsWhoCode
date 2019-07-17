import random

# A list of words that
potential_words = ["vector", "matrix", "sequence", "axis", "derivative", "slope"]

word = random.choice(potential_words)

# Use to test your code:
# print(word)
print(word)
# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
current_word = [] # TIP: the number of letters should match the word
print("Welcome to the Guess the Word game! Hint: These words are math related.")
for character in word:
    current_word.append("_")
print(current_word)

# Some useful variables
guesses = []
maxfails = len(word)+4
fails = 0
correctGuesses = 0

while fails < maxfails:
    # check if the guess is valid: Is it one letter? Have they already guessed it?
    guess = input("Guess a letter: ")
    if guess.isnumeric():
        print("That's not a letter!")
    if guess in guesses:
        print("You already guessed this letter!")
    guesses.append(guess)
	# check if the guess is correct: Is it in the word? If so, reveal the letters!
    for letter in range(0, len(word)):
        if word[letter] == guess:
            current_word[letter] = guess
            correctGuesses += 1
    print(current_word)

    #Victory when current word is original word
    if correctGuesses == len(word):
        print("You win! The word was "+word+"!")
        break

    fails = fails+1
    print("You have " + str(maxfails - fails) + " tries left!")
