import random

def deal_card():
    """ Return a random card from the deck """
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_points(cards):
    """ Take a list of cards and return the points calculated from the cards """
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.remove(1)

    return sum(cards)

def compare_cards(player_final_points, computer_final_points):
    if player_final_points == computer_final_points:
        return "It is a Draw."
    elif computer_final_points == 0:
        return "Lose, your opponent has a Blackjack."
    elif player_final_points == 0:
        return "You win with a Blackjack."
    elif player_final_points > 21:
        return "You lose, as your cards have busted."
    elif computer_final_points > 21:
        return "You win, as your opponent's cards have busted."
    elif player_final_points > computer_final_points:
        return "Congratulations, you win."
    else:
        return "You lose. Try again."

def play_blackjack():
    player_cards = []
    computer_cards = []
    player_point = -1
    computer_point = -1
    is_game_over = False

    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        player_point = calculate_points(player_cards)
        computer_point = calculate_points(computer_cards)

        print(f"Your cards: {player_cards}, and your current total points is {sum(player_cards)}.")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_point == 0 or computer_point == 0 or player_point > 21:
            is_game_over = True
        else:
            continue_to_draw = input("Would you like to draw another card? Type 'y' for yes or 'n' to pass\n").lower()

            if continue_to_draw == "y":
                player_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_point != 0 and computer_point < 17:
        computer_cards.append(deal_card())
        computer_point = calculate_points(computer_cards)

    print(f"Your cards: {player_cards}, final points: {player_point}.")
    print(f"Component's cards: {computer_cards}, final points: {computer_point}.")

    print(compare_cards(player_point, computer_point))

print("Welcome to Py Blackjack!")
while input("Do you want to play a game of Blackjack? Type 'y' for yes and 'n' for no\n").lower() == "y":
    print("\n" * 20)
    play_blackjack()
