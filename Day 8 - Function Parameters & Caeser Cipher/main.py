def greet(name):
    print(f"Good morning, {name.capitalize()}")
    print(f"Good afternoon, {name.capitalize()}")
    print(f"Good evening, {name.capitalize()}")

greet("jeremy")

def greet_with(name, location):
    print(f"Good morning, {name.capitalize()}")
    print(f"How is it be like in {location.capitalize()}?")

greet_with("jeremy", "malaysia")
