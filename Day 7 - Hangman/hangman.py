import random

word_list = ['javascript', 'react', 'debug', 'tailwind', 'python', 'bug', 'programming', 'database']
word_to_guess = random.choice(word_list)

placeholder = ""

if word_to_guess:
    for char in word_to_guess:
        print(char)
        placeholder += "_"

print("Welcome to the Programmer Hanger")
user_input = input("Let's guess a letter\n").lower()

word_display = ""

for char in word_to_guess:
    if user_input == char:
        word_display += char
        print("right")
    else:
        word_display += "_"
        print("wrong")

print(word_display)