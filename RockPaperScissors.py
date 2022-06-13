# this is a program for the rock, paper, scissors game i played when i was young
# we need to import random, to help us randomly select from avaiable options


import random


while True:
    available_options = ['rock', 'paper',  'scissors']
    computer_options = random.choice(available_options)
    user_options = input("Enter Your Weapons: rock, paper, scissors: ")

    if user_options == computer_options:
        print("You choosed " + user_options +
              " computer choosed " + computer_options)
        print("Hence, it is a tie")
    elif user_options == 'rock' and computer_options == "paper":
        print("You LOST")
        print("You entered " + user_options +
              " computer choosed " + computer_options)
    elif user_options == "paper" and computer_options == 'rock':
        print("You WON")
        print("You entered " + user_options +
              " computer choosed " + computer_options)
    elif user_options == "scissors" and computer_options == "paper":
        print("You WON")
        print("You entered " + user_options +
              " computer choosed " + computer_options)
    elif user_options == "paper" and computer_options == "scissors":
        print("You LOST")
        print("You entered " + user_options +
              " computer choosed " + computer_options)
    elif user_options == "rock" and computer_options == "scissors":
        print("You WON")
        print("You entered " + user_options +
              " computer choosed " + computer_options)
    elif user_options == "scissors" and computer_options == "rock":
        print("You LOST")
        print("You entered " + user_options +
              " computer choosed " + computer_options)
    else:
        print("Your Input Is Not Valid")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
