print("Welcome to the Roller Ghoster Ride\n")
height = int(input("What is your height in cm?\n"))
amount_to_pay = 0

if height >= 120:
    print("You can ride the rollercoaster")

    age = int(input("What is your age?\n"))

    if age <= 12:
        amount_to_pay = 6
        print("Child tickets are RM 6")
    elif age <= 18:
        amount_to_pay = 10
        print("Youth tickets are RM 10")
    else:
        amount_to_pay = 14
        print("Adult tickets are RM 14")

    wants_rollercoaster_photography = input("Do you want to have a photo take? Type Y for Yes and N for No.\n")

    if wants_rollercoaster_photography.lower() == "y":
        print("Photo price is another additional RM 3")
        amount_to_pay += 3

    print(f"Your total bill is RM {amount_to_pay}")
    print("Thank you and enjoy your ride!")
else:
    print("Sorry you have to grow taller before you can ride")