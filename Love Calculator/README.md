# ❤️ Love Calculator

This is a fun Python program that calculates a **Love Score** between two names.

The program combines both names and counts the number of times the letters in the words **TRUE** and **LOVE** appear. These two totals are then combined to create the final love score.

> This project is just a fun programming exercise and is not a real measure of compatibility. 😄

## What I Learned

In this project, I practiced:

* Taking user input using `input()`
* Combining strings
* Converting strings using `.lower()`
* Counting characters using `.count()`
* Converting between `int` and `str`
* Using `if`, `elif`, and `else`
* Using logical operators such as `or` and `and`
* Creating conditions using ranges

## How It Works

First, the program asks for two names:

```python
name1 = input("Enter your name:")
name2 = input("Enter your love name:")
```

The names are combined:

```python
both_names = name1 + name2
```

Then converted to lowercase:

```python
new_names = both_names.lower()
```

This allows uppercase and lowercase letters to be treated the same.

## Calculating TRUE

The program counts the letters:

```text
T
R
U
E
```

using:

```python
T = new_names.count('t')
R = new_names.count('r')
U = new_names.count('u')
E = new_names.count('e')

TRUE = T + R + U + E
```

## Calculating LOVE

The same process is used for:

```text
L
O
V
E
```

```python
L = new_names.count('l')
O = new_names.count('o')
V = new_names.count('v')
E = new_names.count('e')

LOVE = L + O + V + E
```

## Creating the Love Score

The two values are joined together:

```python
love_score = int(str(TRUE) + str(LOVE))
```

For example, if:

```text
TRUE = 4
LOVE = 6
```

then:

```text
"4" + "6"
     ↓
   "46"
     ↓
int("46")
     ↓
    46
```

So the final love score is:

```text
46
```

## Conditions

The program checks the final score.

If the score is below `10` or above `90`:

```python
if love_score < 10 or love_score > 90:
```

it displays the **Coke and Mentos** message.

If the score is between `40` and `50`:

```python
elif love_score >= 40 and love_score <= 50:
```

it displays:

```text
You are alright together.
```

Otherwise, it simply displays the love score.

## Complete Code

```python
name1 = input("Enter your name:")

name2 = input("Enter your love name:")

both_names = name1 + name2

new_names = both_names.lower()

T = new_names.count('t')
R = new_names.count('r')
U = new_names.count('u')
E = new_names.count('e')

TRUE = T + R + U + E

L = new_names.count('l')
O = new_names.count('o')
V = new_names.count('v')
E = new_names.count('e')

LOVE = L + O + V + E

love_score = int(str(TRUE) + str(LOVE))

if love_score < 10 or love_score > 90:

    print(
        f"Your love score is {love_score} "
        "and you will go like coke and mentos."
    )

elif love_score >= 40 and love_score <= 50:

    print(
        f"Your love score is {love_score} "
        "and you are alright together."
    )

else:

    print(f"Your love score is {love_score}.")
```

## Program Flow

```text
Enter Name 1
     ↓
Enter Name 2
     ↓
Combine both names
     ↓
Convert to lowercase
     ↓
Count T + R + U + E
     ↓
Count L + O + V + E
     ↓
Combine both counts
     ↓
Generate Love Score
     ↓
Check conditions
     ↓
Display Result ❤️
```

## Example Output

```text
Enter your name: Alex
Enter your love name: Taylor

Your love score is 42 and you are alright together.
```

The result depends entirely on the letters present in the two entered names.

Through this exercise, I practiced string manipulation, `.count()`, type conversion, logical operators, and conditional statements by building a fun Love Calculator.
