# 🔢 FizzBuzz

This is a simple Python program that implements the classic **FizzBuzz** problem.

The program takes a number from the user and prints numbers from `1` up to the entered number while replacing certain numbers with **Fizz**, **Buzz**, or **Fizz Buzz**.

## What I Learned

In this project, I practiced:

* Taking user input using `input()`
* Converting input using `int()`
* Using `for` loops
* Using `range()`
* Using `if`, `elif`, and `else`
* Using the modulus operator `%`
* Using the logical `and` operator
* Checking divisibility of numbers

## FizzBuzz Rules

For every number:

* If the number is divisible by `3` → Print `Fizz`
* If the number is divisible by `5` → Print `Buzz`
* If the number is divisible by both `3` and `5` → Print `Fizz Buzz`
* Otherwise → Print the number

## Code

```python
number = int(input("Enter the number: "))

for i in range(1, number + 1):

    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)
```

## How It Works

The loop:

```python
for i in range(1, number + 1):
```

starts from `1` and continues up to the number entered by the user.

For example, if:

```text
number = 15
```

the loop processes:

```text
1, 2, 3, 4, 5, 6, ... 15
```

The `%` operator is used to check divisibility.

For example:

```python
i % 3 == 0
```

means the number is completely divisible by `3`.

## Example Output

If the user enters:

```text
Enter the number: 15
```

Output:

```text
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
Fizz Buzz
```

## Important Logic

The condition for both `3` and `5` is checked **first**:

```python
if i % 3 == 0 and i % 5 == 0:
```

This is important because a number like `15` is divisible by both `3` and `5`.

If we checked:

```python
if i % 3 == 0:
```

first, Python would print `Fizz` for `15` and would never reach the check for both numbers.
.

Through this exercise, I practiced loops, conditional statements, logical operators, and the modulus operator by solving the classic FizzBuzz problem.
