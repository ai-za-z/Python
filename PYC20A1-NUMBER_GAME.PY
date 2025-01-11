import random
Play = True
number = str(random.randint(0,10))
print("Guess the right number between 0 and 10...")
print("You have only one choice....")




while Play:
    guess = input("Enter your guess..")
    if guess == number:
        print(f"You guess it right", (number))
        break 
    else:
        print("You lost the game..")
        