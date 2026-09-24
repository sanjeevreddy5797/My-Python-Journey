# 📈 Higher Lower Game

A command-line **Higher Lower Game** built using Python as part of my **100 Days of Python** learning journey.

The player is shown two famous people, brands, or social-media accounts and must guess which one has more followers.

Every correct answer increases the score. The game continues until the player makes a wrong guess.

## 🎯 How the Game Works

The program randomly selects two accounts:

```text
Compare A: Cristiano Ronaldo, a Footballer, from Portugal.

VS

Compare B: Taylor Swift, a Musician, from United States.
```

The player chooses:

```text
A
```

or:

```text
B
```

The program compares their follower counts.

If the answer is correct:

```text
You're right! Current score: 1
```

If the answer is incorrect:

```text
Sorry, that's wrong. Final score: 1
```

and the game ends.

## 🧠 Concepts I Practiced

Through this project, I practiced:

* Python functions
* Function parameters
* Return values
* Dictionaries
* Lists of dictionaries
* Accessing dictionary values
* `while` loops
* Nested `while` loops
* `if / else`
* Boolean values
* `random.choice()`
* Importing data from another Python file
* Importing ASCII art
* Keeping track of a score
* Comparing values
* Updating variables during a game

## 📁 Project Structure

```text
Higher-Lower-Game/
│
├── main.py
├── game_data.py
└── art.py
```

### `main.py`

Contains the main game logic.

### `game_data.py`

Contains the account information:

```python
data = [
    {
        "name": "...",
        "follower_count": ...,
        "description": "...",
        "country": "..."
    }
]
```

### `art.py`

Contains:

```python
logo
vs
```

which are used to display the game's ASCII art.

## 📦 Importing the Required Data

```python
from art import logo, vs
from game_data import data
import random
```

`logo` and `vs` are imported from `art.py`.

`data` is imported from `game_data.py`.

The `random` module is used to randomly select accounts.

## 🎲 Selecting Account A

Before the main loop starts:

```python
account_a = random.choice(data)
```

Suppose Python randomly chooses:

```python
{
    "name": "Cristiano Ronaldo",
    "follower_count": 215,
    "description": "Footballer",
    "country": "Portugal"
}
```

This dictionary becomes `account_a`.

## 🎲 Selecting Account B

Inside the game loop:

```python
account_b = random.choice(data)
```

Another random account is selected.

However, there is a possibility that:

```python
account_a == account_b
```

So the program checks:

```python
while account_a == account_b:
    account_b = random.choice(data)
```

This ensures that the same account is never compared against itself.

## 📝 Formatting Account Information

The `format_data()` function converts the account dictionary into a readable sentence:

```python
def format_data(account):

    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_descr}, from {account_country}"
```

For example:

```python
account = {
    "name": "Cristiano Ronaldo",
    "follower_count": 215,
    "description": "Footballer",
    "country": "Portugal"
}
```

becomes:

```text
Cristiano Ronaldo, a Footballer, from Portugal
```

Notice that the follower count is intentionally **not displayed**, because the player needs to guess which account has more followers.

## ⚔️ Checking the Player's Answer

The answer is checked using:

```python
def check_answer(user_guess, a_followers, b_followers):

    if a_followers > b_followers:
        return user_guess == "a"

    else:
        return user_guess == "b"
```

Suppose:

```text
A followers = 215
B followers = 150
```

Since:

```text
215 > 150
```

the correct answer is:

```text
A
```

If the player entered:

```text
a
```

then:

```python
user_guess == "a"
```

becomes:

```text
True
```

Therefore:

```python
is_correct = True
```

## 🔢 Tracking the Score

The score starts at:

```python
score = 0
```

Every correct answer increases it:

```python
score += 1
```

For example:

```text
Start

score = 0

Correct → score = 1

Correct → score = 2

Correct → score = 3

Wrong → Game Over
```

## 🔄 Moving the Winner to Account A

After a correct answer, your program checks:

```python
if b_follower_count > a_follower_count:
    account_a = account_b
```

This means if **B had more followers**, B becomes A for the next round.

Example:

```text
Round 1

A = Person X → 100M
B = Person Y → 200M

Player chooses B ✅
```

Now:

```python
account_a = account_b
```

So the next round becomes:

```text
A = Person Y → 200M
B = New random account
```

However, if A already had more followers, your code keeps the existing A.

## 💻 Complete Code

```python
from art import logo, vs
from game_data import data
import random


def format_data(account):

    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]

    return (
        f"{account_name}, a {account_descr}, "
        f"from {account_country}"
    )


def check_answer(user_guess, a_followers, b_followers):
    """Check whether the user's Higher Lower guess is correct."""

    if a_followers > b_followers:
        return user_guess == "a"

    else:
        return user_guess == "b"


print(logo)

score = 0
condition = True

account_a = random.choice(data)


while condition:

    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")

    print(vs)

    print(f"Compare B: {format_data(account_b)}.")

    guess = input(
        "Who has more followers? Type 'A' or 'B': "
    ).lower()

    print("\n" * 20)

    print(logo)

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(
        guess,
        a_follower_count,
        b_follower_count
    )

    if is_correct:

        score += 1

        print(
            f"You're right! Current score: {score}"
        )

        if b_follower_count > a_follower_count:
            account_a = account_b

    else:

        print(
            f"Sorry, that's wrong. Final score: {score}"
        )

        condition = False
```

## 🔄 Game Flow

```text
                 START
                   ↓
             Display Logo
                   ↓
          Select Random A
                   ↓
          Select Random B
                   ↓
             Is A == B?
              /       \
            YES        NO
             ↓          ↓
        Select B      Continue
          Again
             \          /
              ↓        ↓
           Display A & B
                   ↓
              User Guess
              A or B?
                   ↓
          Get Follower Counts
                   ↓
            Compare Counts
                   ↓
          Is Guess Correct?
             /         \
           YES          NO
            ↓            ↓
       score += 1     Game Over
            ↓
      Which account
      has more followers?
            ↓
      Keep winner as A
            ↓
      Generate New B
            ↓
        Next Round
```

## 🖥️ Example Output

```text
---------- Higher Lower Game ----------

Compare A:
Cristiano Ronaldo, a Footballer, from Portugal.

VS

Compare B:
Taylor Swift, a Musician, from United States.

Who has more followers?
Type 'A' or 'B': A

You're right! Current score: 1

Compare A:
Cristiano Ronaldo, a Footballer, from Portugal.

VS

Compare B:
National Geographic, a Magazine, from United States.

Who has more followers?
Type 'A' or 'B': A

You're right! Current score: 2
```

If the next answer is wrong:

```text
Sorry, that's wrong. Final score: 2
```

## 🔑 Important Concept — List of Dictionaries

The `data` variable contains multiple dictionaries inside a list:

```python
data = [
    {
        "name": "Account A",
        "follower_count": 100,
        "description": "Musician",
        "country": "United States"
    },
    {
        "name": "Account B",
        "follower_count": 200,
        "description": "Footballer",
        "country": "Portugal"
    }
]
```

So:

```python
random.choice(data)
```

returns one complete dictionary.

Then:

```python
account_a["name"]
```

gets the name.

```python
account_a["description"]
```

gets the description.

```python
account_a["country"]
```

gets the country.

```python
account_a["follower_count"]
```

gets the follower count.

This project helped me understand how **lists and dictionaries can work together to represent structured data**.

## 🚀 Future Improvements

I can improve this project by:

* Validating that the user enters only `A` or `B`
* Adding a restart option
* Keeping track of the highest score
* Preventing recently used accounts from appearing again
* Adding more accounts
* Improving the terminal interface
* Organizing the game using OOP
* Using updated follower data from an API


Through this project, I practiced combining:

```text
Functions
   +
Dictionaries
   +
Lists
   +
Random Selection
   +
While Loops
   +
Conditional Logic
   +
Score Tracking
        ↓
Higher Lower Game 📈
```

One of the biggest lessons from this project was learning how to work with structured data and how to carry information from one game round into the next.
