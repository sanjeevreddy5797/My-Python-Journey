# 🃏 Blackjack Game

A command-line **Blackjack game built with Python** as part of my **100 Days of Python** learning journey.

The player competes against the computer and tries to get a score as close to **21** as possible without going over.

## 🎯 How the Game Works

* The player and computer receive **2 cards** at the beginning.
* The player can choose to:

  * `y` → Draw another card
  * `n` → Pass
* If the player's score goes above `21`, the player loses.
* After the player's turn, the computer draws cards until its score reaches at least `17`.
* The final scores are compared to determine the winner.

## 🧠 Concepts I Practiced

This project helped me practice:

* Functions
* Function parameters
* Return values
* Lists
* `while` loops
* `for` loops
* `if / elif / else`
* Boolean variables
* `random.choice()`
* `sum()`
* `.append()`
* `.remove()`
* Game logic
* Breaking a large program into smaller functions

## 🃏 Card Values

The deck is represented as:

```python
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
```

Card values:

```text
Ace              → 11 or 1
2–9              → Face value
10               → 10
Jack             → 10
Queen            → 10
King             → 10
```

## 🎲 `deal_card()`

This function returns one random card:

```python
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
```

For example:

```python
deal_card()
```

could return:

```text
7
```

## 🧮 `calculate_score()`

This function calculates the total score of a hand.

```python
def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
```

### Blackjack

If the player gets:

```text
[11, 10]
```

the total is `21` with exactly two cards.

The program returns:

```python
0
```

Here, `0` is a special value used to represent **Blackjack**.

### Handling the Ace

An Ace initially has a value of `11`.

For example:

```text
[11, 10, 5]

11 + 10 + 5 = 26
```

Since `26 > 21`, the Ace changes from `11` to `1`:

```text
[1, 10, 5]

1 + 10 + 5 = 16
```

This prevents the player from going over 21 when the Ace can legally be counted as 1.

## ⚔️ `compare()`

The `compare()` function determines the winner.

```python
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
```

It checks for:

* Draw
* Computer Blackjack
* Player Blackjack
* Player going over 21
* Computer going over 21
* Player having the higher score
* Computer having the higher score

## 🤖 Computer Logic

The computer keeps drawing cards while its score is below `17`:

```python
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
```

For example:

```text
Computer cards: [10, 5]
Score: 15

15 < 17
↓
Draw another card
```

If the next card is `2`:

```text
[10, 5, 2]

Score = 17
```

The computer stops drawing.

## 💻 Complete Code

```python
import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


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

    # Deal two cards
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

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        else:

            choice = input(
                "Type 'y' to get another card, "
                "type 'n' to pass: "
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


while input(
    "\nDo you want to play Blackjack? Type 'y' or 'n': "
).lower() == "y":

    play_game()


print("Thanks for playing Blackjack!")
```

## 🔄 Program Flow

```text
START
  ↓
Play Blackjack?
  ↓
Deal 2 Cards Each
  ↓
Calculate Scores
  ↓
Show Player's Cards
  ↓
Show Computer's First Card
  ↓
Player Blackjack / Over 21?
  │
  ├── Yes → End Player Turn
  │
  └── No
       ↓
     Hit?
    /    \
  Yes     No
   ↓       ↓
Draw     Pass
Card
   ↓
Calculate Again
   ↓
Computer's Turn
   ↓
Score < 17?
  /      \
Yes       No
 ↓         ↓
Draw     Compare
Card      Scores
           ↓
       Show Winner
           ↓
       Play Again?
```

## 🖥️ Example Output

```text
Do you want to play Blackjack? Type 'y' or 'n': y

Your cards: [10, 7]
Your current score: 17
Computer's first card: 9

Type 'y' to get another card, type 'n' to pass: y

Your cards: [10, 7, 3]
Your current score: 20
Computer's first card: 9

Type 'y' to get another card, type 'n' to pass: n

------------------------------
Your final hand: [10, 7, 3]
Your final score: 20

Computer's final hand: [9, 8]
Computer's final score: 17

You win 😎
------------------------------
```

## 📁 Project Structure

```text
100-days-python/
│
└── Blackjack/
    ├── main.py
    └── README.md
```


The main lesson from this project was learning how multiple functions can work together to create a complete program:

```text
deal_card()
     ↓
calculate_score()
     ↓
compare()
     ↓
play_game()
```

Instead of writing all the logic in one place, each function performs a specific job. This makes the program easier to understand, debug, and improve.
