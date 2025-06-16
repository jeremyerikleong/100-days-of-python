print("Welcome to Name Formatter")
first_name = input("Enter your first name\n")
last_name = input("Enter your last name\n")

def format_name(f_name, l_name):
    return f"{f_name.title()} {l_name.title()}"


print(format_name(first_name, last_name))