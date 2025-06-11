print(type("python"))
print(type(123))
print(type(1.68))
print(type(True))

# convert number to strings
user_input = input("Enter your name\n")
length_of_user_input = len(user_input)
print("Number of letters in your name: " + str(length_of_user_input))

# bmi
height = input("What is your height in m?\n")
weight = input("What is your weight in kg?\n")

bmi = float(weight) / (float(height) ** 2)
print(f"Your BMI is: {round(bmi, 2)}")
