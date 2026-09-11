# 🎲 Who Will Pay the Bill?

This is a simple Python program that randomly selects one person from a list of friends to **pay the bill**. 😄

In this program, I learned two different ways to randomly select an item from a Python list.

## What I Learned

In this project, I practiced:

* Importing the `random` module
* Creating and using Python lists
* Accessing list elements using indexes
* Generating random integers using `random.randint()`
* Selecting random elements using `random.choice()`
* Using f-strings to display the result

## Friends List

The program contains a list of friends:

```python
friends = [
    "Sanjeev",
    "Kailash",
    "Rupa",
    "Karunkar",
    "Viraaj",
    "Joy"
]
```

The program randomly chooses one person from this list to pay the bill.

## Method 1 - Using `random.randint()`

```python
number = random.randint(0, 5)

print(f"{friends[number]} has to pay the bill.")
```

`random.randint(0, 5)` generates a random number between `0` and `5`.

Since the list contains 6 elements, their indexes are:

```text
0 → Sanjeev
1 → Kailash
2 → Rupa
3 → Karunkar
4 → Viraaj
5 → Joy
```

The randomly generated number is then used as the index of the list.

For example:

```text
Random number = 3

friends[3]
    ↓
Karunkar
```

So the output would be:

```text
Karunkar has to pay the bill.
```

## Method 2 - Using `random.choice()`

Python provides an easier way to randomly select an element from a list:

```python
print(f"{random.choice(friends)} has to pay the bill.")
```

`random.choice(friends)` directly chooses a random person from the list.

So we don't need to manually generate an index.

## Complete Code

```python
import random

friends = ["Sanjeev", "Kailash", "Rupa", "Karunkar", "Viraaj", "Joy"]

# 1st option to solve the problem
number = random.randint(0, 5)

print(f"{friends[number]} has to pay the bill.")

# 2nd option to solve the problem
print(f"{random.choice(friends)} has to pay the bill.")
```

## Example Output

```text
Viraaj has to pay the bill.
Rupa has to pay the bill.
```

Since both methods make their **own random selection**, the two outputs can contain different names.

## Better Approach

Between the two approaches, I prefer:

```python
random.choice(friends)
```

because it is simpler and doesn't require knowing the list's indexes.

Also, if more friends are added later, `random.choice()` will continue working without changing `0, 5`.


Through this exercise, I learned how Python can randomly select values from a list using the `random` module.
