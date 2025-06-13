import random
import word_list

word_to_guess = random.choice(word_list.lists)

placeholder = ""

if word_to_guess:
    for char in word_to_guess:
        placeholder += "_"

print("Welcome to the Programmer Hanger")

lives = 5
correct_guess = []

while lives > 0:
    user_input = input("Let's guess a letter\n").lower()

    word_display = ""

    for char in word_to_guess:
        if user_input == char:
            word_display += char
            correct_guess.append(char)
        elif char in correct_guess:
            word_display += char
        else:
            word_display += "_"

    print(word_display)

    if user_input not in correct_guess:
        lives -= 1
        print(f'You guessed {user_input}, which is not inside the word. Hence you lost a life.')
        print(f'=====================remaining {lives}/5 lives ============================')

        if lives == 0:
            print("Game Over! You have lost all your lives.")

    if "_" not in word_display:
        print("Yay, You win!")
