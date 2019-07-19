# --- Define your functions below! ---
import random
def intro():
    print("Hi! Welcome to ChatBot!")
    print("Tell us something interesting about yourself.")

def process_input(answer):
    if is_valid_input(answer):
        say_greeting()
    else:
        say_default()

def is_valid_input(word):
    word = word.lower()
    valid_greetings = ["hi", "hey", "hello", "hiya", "sup", "suh", "howdy"]
    if word in valid_greetings:
        return True
    else:
        return False

def say_greeting():
    print("Hello, I'm ChatBot!")

def say_default():
    print("Thank you Kanye, very cool!")

def process_day(day):
    if is_valid_day(day):
        say_day1()
    else:
        say_daydefault()

def is_valid_day(day1):
    day1 = day1.lower()
    valid_day = ["it's good", "its good", "great", "good", "amazing", "wonderful", "fun"]
    if day1 in valid_day:
        return True
    else:
        return False

def say_day1():
    print("That's great!")

def say_day2():
    print("Aw, I'm sorry. It's not the end of the world, if that helps.")

def say_daydefault():
    print("It be like that sometimes.")

def process_python(python):
    if is_valid_python(python) == "Good":
        print("That's great! I think python is fun too.")
    elif is_valid_python(python) == "Bad":
        print("Don't worry, it just takes a little bit of practice until things start to click.")
    else:
        print("I concur.")

def is_valid_python(python1):
    python1 = python1.lower()
    valid_pythonsGood = ["I like it", "its fun", "its good", "its ok", "fun", "good", "its great", "its amazing"]
    valid_pythonsBad = ["i dont like it", "i don't like it", "its hard", "it's hard", "boring", "hard"]
    if python1 in valid_pythonsGood:
        return "Good"
    elif python1 in valid_pythonsBad:
        return "Bad"
    else:
        return False

def process_game(game):
    if game == "yes":
        print("Yay! Let's play rock, paper, scissors.")
        potential_choices = ["rock", "paper", "scissors"]
        botChoice = random.choice(potential_choices)
        print("Ready?")
        userChoice = input("Make your choice: ")
        userChoice = userChoice.lower()
        print("Rock, paper, scissors, shoe! I choose... "+botChoice+"!")

        if botChoice == "rock" and userChoice == "paper":
            print("Aw. Paper beats rock, you win.")
        elif botChoice == "rock" and userChoice == "scissors":
            print("Hah! Rock beats scissors, I win!")
        elif botChoice == "paper" and userChoice == "rock":
            print("Yes! Paper beats rock, I win!")
        elif botChoice == "paper" and userChoice == "scissors":
            print("Scissors beats paper, you win.")
        elif botChoice == "scissors" and userChoice == "rock":
            print("Rock beats scissors. You win.")
        elif botChoice == "scissors" and userChoice == "paper":
            print("Scissors beats paper, I win!")
        elif botChoice == userChoice:
            print("Both of us chose "+botChoice+"! No winners this time.")
    else:
        print("That's ok, maybe we can play another time.")

# --- Put your main program below! ---
def main():
  intro()
  while True:
    answer = input("(What will you say?) ")
    process_input(answer)

    name = input("What is your name?")
    print("Nice to meet you, "+name+"!")

    day = input("How was your day?")
    process_day(day)

    python = input("How are you enjoying python so far?")
    process_python(python)

    game = input("Do you want to play a game?")
    process_game(game)

    break
# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
