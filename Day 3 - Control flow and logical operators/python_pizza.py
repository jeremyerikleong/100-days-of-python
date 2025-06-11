print("Welcome to Python Pizza Deliveries!")

print("Small pizza (S): RM 15\nMedium pizza (M): RM 20\nLarge Pizza (L): RM 25")
pizza_size = input("What size pizza do you want? S, M or L:\n")
wants_pepperoni = input("Do you want pepperoni on your pizza? Y for yes and N for no:\n")
extra_cheese = input("Do you want extra cheese? Y for yes and N for no:\n")
amount_to_pay = 0

# pizza size condition checking
if pizza_size.upper() == "S":
    amount_to_pay += 12
elif pizza_size.upper() == "M":
    amount_to_pay += 15
elif pizza_size.upper() == "L":
    amount_to_pay += 25
else:
    print("Sorry, We only have these 3 pizza sizes available.")

# pepperoni condition checking
if wants_pepperoni.upper() == "Y":
    if pizza_size.upper() == "S":
        amount_to_pay += 2
    else:
        amount_to_pay += 3

# cheese addon condition checking
if extra_cheese.upper() == "Y":
    amount_to_pay += 1

print(f"Your bill is RM {amount_to_pay}")