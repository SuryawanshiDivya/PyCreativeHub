import random


def num_guessing_game():
    secret_nuumber=random.randint(1, 100)
    guess=None

    print("Welcome to the game")
    print("GUess number between 1 to 100")
    print("can you guess it?")

    while guess!=secret_nuumber:
         guess=int(input("Enter the guess"))

         if guess<secret_nuumber:
             print("Too low, try again")

         elif( guess>secret_nuumber):
            print("Too high, try again")

         else:
            print("You guessed correct number!!!! :)")

num_guessing_game()