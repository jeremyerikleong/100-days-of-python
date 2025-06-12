import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','u','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','(',')','*','+','-','=']

print("Welcome to the PyPassword Generator!")
num_of_letters = int(input("How many letters would you like in your password?\n"))
num_of_symbols = int(input("How many symbols?\n"))
num_of_numbers = int(input("How many numbers?\n"))

password_list = []
for letter in range(1, num_of_letters + 1):
    random_character = random.choice(letters)
    password_list.append(random_character)

for number in range(1, num_of_numbers + 1):
    random_number = random.choice(numbers)
    password_list.append(random_number)

for symbol in range(1, num_of_symbols + 1):
    random_symbol = random.choice(symbols)
    password_list.append(random_symbol)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is {password}")