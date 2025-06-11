print("Welcome to Treasure Island")
print("Yout mission is to find the treasure")

path = input('You\'re at the crossroad, where do you to go? Type "left" or "right".\n').lower()

if path == "left":
    print("You've come to a lake, there a boat right over the jetty there")
    option = input('Do you want take the boat or swim across? Type "take" to take the boat or "swim" to swim across the lake.\n').lower()

    if option == "take":
        door = input("You arrived to the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n").lower()

        if door == "red":
            print("It is a room full of fire. Game Over.")
        elif door == "yellow":
            print("You've found the treasure. You Win!")
        elif door == "blue":
            print("You entered a room full of sea monsters. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attack by the freshwater crocodile. Game Over.")
else:
    print("You've fell into the trap. Game Over.")
