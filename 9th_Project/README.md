# 🔐 Random Password Generator

This is a simple Python program that generates a **random password** based on the user's requirements.

The user can decide how many **numbers, special characters, and letters** should be included in the password. The program randomly selects them, shuffles their order, and generates the final password.

## What I Learned

In this project, I practiced:

* Using the `random` module
* Working with Python lists
* Using `for` loops
* Using `range()`
* Using `random.choice()`
* Using `random.shuffle()`
* Adding elements using `.append()`
* Using `len()`
* Building strings using concatenation
* Taking user input using `input()`
* Converting input using `int()`

## How It Works

The program asks the user to enter:

1. Number of digits
2. Number of special characters
3. Number of letters

For example:

```text
Numbers: 3
Characters: 2
Letters: 5
```

The final password will contain:

```text
3 Numbers + 2 Special Characters + 5 Letters
                  ↓
          10-character password
```

## Code

```python
import random

numbers = ['0','1','2','3','4','5','6','7','8','9']

characters = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+',
    '[', ']', '{', '}',
    ';', ':', "'", '"',
    ',', '<', '.', '>',
    '/', '?', '\\', '|'
]

words = [
    'a','b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J',
    'K','L','M','N','O','P','Q','R','S','T',
    'U','V','W','X','Y','Z'
]

print("----------Welcome to the password generator----------")

n_numbers = int(input(
    "Enter the no of numbers you want to have in your password:"
))

n_characters = int(input(
    "Enter the no of characters you want to have in your password:"
))

n_words = int(input(
    "Enter the no of words you want to have in your password:"
))

password = []

for i in range(0, n_numbers):
    password.append(random.choice(numbers))

for i in range(0, n_characters):
    password.append(random.choice(characters))

for i in range(0, n_words):
    password.append(random.choice(words))

random.shuffle(password)

new_password = ''

for i in range(len(password)):
    new_password += password[i]

print(f"Your Password is {new_password}")
```

## Program Flow

```text
START
  ↓
Ask number of digits
  ↓
Ask number of special characters
  ↓
Ask number of letters
  ↓
Randomly select digits
  ↓
Randomly select special characters
  ↓
Randomly select letters
  ↓
Store everything in a list
  ↓
Shuffle the list
  ↓
Convert the list into a string
  ↓
Display Password 🔐
```

## Why `random.choice()`?

The program uses:

```python
random.choice(numbers)
```

to randomly select one item from a list.

For example:

```python
numbers = ['0', '1', '2', '3']
```

`random.choice(numbers)` might return:

```text
'2'
```

Each call can produce a different result.

## Why `random.shuffle()`?

Initially, the password list is created in groups:

```text
Numbers → Characters → Letters
```

For example:

```text
['5', '8', '2', '@', '#', 'A', 'k', 'P']
```

Using:

```python
random.shuffle(password)
```

changes the order randomly:

```text
['k', '5', '@', 'P', '2', 'A', '#', '8']
```

The resulting password becomes:

```text
k5@P2A#8
```

## Example Output

```text
----------Welcome to the password generator----------

Enter the no of numbers you want to have in your password: 3
Enter the no of characters you want to have in your password: 2
Enter the no of words you want to have in your password: 5

Your Password is K7@p3#A1xz
```

Every execution can generate a different password.


Through this project, I practiced Python lists, loops, random selection, list shuffling, and string manipulation by building a random password generator.
