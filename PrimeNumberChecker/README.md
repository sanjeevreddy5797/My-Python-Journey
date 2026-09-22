# 🔢 Prime Number Checker

A simple **Prime Number Checker** built using Python as part of my **100 Days of Python** learning journey.

The program takes a number from the user and determines whether it is:

* A **Prime Number**
* A **Composite Number**
* Neither prime nor composite (`1`)

## 🎯 What is a Prime Number?

A **prime number** is a number greater than `1` that has exactly **two factors**:

1. `1`
2. The number itself

For example:

```text
7
```

The factors of `7` are:

```text
1, 7
```

Since it has exactly `2` factors:

```text
7 is a Prime Number.
```

## Composite Number

A composite number has more than two factors.

For example:

```text
6
```

Its factors are:

```text
1, 2, 3, 6
```

Since it has more than two factors:

```text
6 is not a Prime Number.
```

## 🧠 Concepts I Practiced

Through this project, I practiced:

* Creating functions
* Function parameters
* `for` loops
* `range()`
* `if / elif / else`
* Modulus operator `%`
* Counters
* User input
* Type conversion using `int()`
* Finding factors of a number

## 💻 Complete Code

```python
print("----------Welcome to Prime Number Checker-----------")


def is_prime(number):

    count = 0

    for i in range(1, number + 1):

        if number % i == 0:
            count += 1

    if number == 1:

        print(
            f"{number} is neither Prime nor Composite Number."
        )

    elif count <= 2:

        print(f"{number} is a Prime Number.")

    else:

        print(f"{number} is not a Prime Number.")


is_prime(
    int(
        input(
            "Enter the number that you want to know "
            "whether it is Prime or Not: "
        )
    )
)
```

## 🔍 How the Program Works

Suppose the user enters:

```text
7
```

The loop runs:

```python
for i in range(1, number + 1):
```

Since:

```text
number = 7
```

it checks:

```text
1
2
3
4
5
6
7
```

For every number, this condition is checked:

```python
if number % i == 0:
```

If the remainder is `0`, then `i` is a factor.

## Example: Checking 7

The program performs:

```text
7 % 1 = 0  → Factor ✅
7 % 2 = 1
7 % 3 = 1
7 % 4 = 3
7 % 5 = 2
7 % 6 = 1
7 % 7 = 0  → Factor ✅
```

Therefore:

```text
count = 2
```

Since `7` has exactly two factors:

```text
7 is a Prime Number.
```

## Example: Checking 6

For:

```text
number = 6
```

the factors are:

```text
1
2
3
6
```

So:

```text
count = 4
```

Since it has more than two factors:

```text
6 is not a Prime Number.
```

## Why `%` is Important

The modulus operator `%` returns the remainder after division.

For example:

```python
10 % 2
```

returns:

```text
0
```

This tells us that `2` divides `10` exactly.

Therefore:

```text
2 is a factor of 10
```

But:

```python
10 % 3
```

returns:

```text
1
```

Therefore:

```text
3 is not a factor of 10
```

## 🔄 Program Flow

```text
START
  ↓
Enter Number
  ↓
Set count = 0
  ↓
Check numbers from 1 to number
  ↓
Is number % i == 0?
   /              \
 YES               NO
  ↓                 ↓
count += 1        Continue
   \               /
    ↓             ↓
     Continue Loop
          ↓
      Is number 1?
       /        \
     YES         NO
      ↓           ↓
Neither Prime   Check Factor Count
nor Composite       ↓
                count == 2?
                 /       \
               YES        NO
                ↓          ↓
              Prime    Not Prime
```

## 🖥️ Example Output

### Prime Number

```text
----------Welcome to Prime Number Checker-----------

Enter the number that you want to know whether it is Prime or Not: 13

13 is a Prime Number.
```

### Composite Number

```text
Enter the number that you want to know whether it is Prime or Not: 12

12 is not a Prime Number.
```

### Number 1

```text
Enter the number that you want to know whether it is Prime or Not: 1

1 is neither Prime nor Composite Number.
```

## ⚡ Possible Optimization

The current program checks every number from:

```text
1 → number
```

For example, if the number is:

```text
1000
```

the loop performs around `1000` checks.

As I learn more about algorithms and DSA, I can optimize the prime-checking process by checking fewer numbers, such as only checking divisors up to the square root of the number.

## 📁 Project Structure

```text
100-days-python/
│
└── Prime-Number-Checker/
    ├── main.py
    └── README.md
```

## 🚀 Future Improvements

Future improvements can include:

* Handling negative numbers
* Handling `0`
* Optimizing the algorithm
* Returning `True` or `False` from `is_prime()`
* Checking multiple numbers
* Finding all prime numbers within a range

Through this project, I practiced functions, loops, conditional statements, counters, and the modulus operator while learning how prime numbers can be identified by counting their factors.
