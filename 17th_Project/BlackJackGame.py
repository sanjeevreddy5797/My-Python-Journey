import random

# Return a random card from the deck
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


# Calculate the total score of the cards
def calculate_score(cards):

    # Blackjack: Ace + 10
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # If Ace is counted as 11 and score goes above 21,
    # change Ace from 11 to 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


# Compare user's score and computer's score
def compare(user_score, computer_score):

    if user_score == computer_score:
        return "Draw 😐"

    elif computer_score == 0:
        return "You lose! Computer has Blackjack 😭"

    elif user_score == 0:
        return "You win with a Blackjack! 😎"

    elif user_score > 21:
        return "You went over 21. You lose 😭"

    elif computer_score > 21:
        return "Computer went over 21. You win 😎"

    elif user_score > computer_score:
        return "You win 😎"

    else:
        return "You lose 😭"


def play_game():

    user_cards = []
    computer_cards = []

    computer_score = -1
    user_score = -1

    is_game_over = False

    # Give 2 cards to user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # User's turn
    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}")
        print(f"Your current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check whether game should end
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        else:
            choice = input(
                "Type 'y' to get another card, type 'n' to pass: "
            ).lower()

            if choice == "y":
                user_cards.append(deal_card())

            else:
                is_game_over = True

    # Computer's turn
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Final result
    print("\n------------------------------")
    print(f"Your final hand: {user_cards}")
    print(f"Your final score: {user_score}")

    print(f"Computer's final hand: {computer_cards}")
    print(f"Computer's final score: {computer_score}")

    print(compare(user_score, computer_score))
    print("------------------------------")


# Keep playing until user says no
while input("\nDo you want to play Blackjack? Type 'y' or 'n': ").lower() == "y":
    play_game()

print("Thanks for playing Blackjack!")