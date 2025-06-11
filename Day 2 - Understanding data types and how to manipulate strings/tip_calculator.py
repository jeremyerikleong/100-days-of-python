print("Welcome to the tip calculator!")
total_bill = input("What is the total bill?\n")
tip = input("How much tip would you like to give? 10,12, or 15?\n")
total_pax = input("How many people to split the bill?\n")

amount_to_pay = (float(total_bill) + (float(total_bill) * int(tip) / 100)) / int(total_pax)
print(f"Each person should pay: ${round(amount_to_pay,2)}")



