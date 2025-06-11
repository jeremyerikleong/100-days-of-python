#Check whether the number is even or odd
number = int(input("Enter a number\n"))

if number % 2 == 0:
    print("this is a even number")
else:
    print("this is an odd number")


# BMI Calculator with Interpretations
height = float(input("What is your height in m?\n"))
weight = float(input("What is your weight in kg?\n"))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"Your bmi score is {round(bmi,2)}, and you are currently underweight")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your bmi score is {round(bmi,2)}, and you are in normal weight")
else:
    print(f"Your bmi score is {round(bmi,2)}, and you are currently overweight")
