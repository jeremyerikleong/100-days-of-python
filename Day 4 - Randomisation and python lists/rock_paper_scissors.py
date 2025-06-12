import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Welcome to Rock, Paper, Scissors game")

option = ["rock", "paper", "scissors"]
game_images = [rock, paper, scissors]
user_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if user_option >= 0 and user_option <= 2:
    print("You chose:")
    print(game_images[user_option])

comp_option = random.randint(0, len(option) - 1)
print("Computer chose:")
print(game_images[comp_option])

if user_option >= 3 or user_option < 0:
    print("You entered an invalid number. You lose!")
elif user_option == 0 and comp_option == 2:
    print("You wins!")
elif comp_option == 0 and user_option == 2:
    print("You lose!")
elif comp_option > user_option:
    print("computer wins!")
elif user_option > comp_option:
    print("You wins!")
elif comp_option == user_option:
    print("It is a draw.")