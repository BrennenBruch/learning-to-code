import random

while True:
    number = random.randint(1, 10)

    number_guessed = int(input("Guess a number from 1-10: "))

    while number_guessed < 1 or number_guessed > 10:
        print("Not a number between 1-10")
        number_guessed = int(input("Guess a number from 1-10: "))

    if number_guessed == number:
        print(f"You got it right! You guessed {number_guessed} and the number was {number}")
    else:
        print(f"You got it wrong! You guessed {number_guessed} and the number was {number}")
    
    play_again = input("Would you like to play again? y or n: ")

    while play_again not in ("y", "n"):
        print("Please type 'y' or 'n'")
        play_again = input("Would you like to play again? y or b: ")

    if play_again == "n":
        print("Thanks for playing")
        break