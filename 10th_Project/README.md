# 🎨 Paint Area Calculator

This is a simple Python program that calculates the **number of paint cans required to paint a wall** based on the wall's height, width, and the area covered by one paint can.

The program uses `math.ceil()` to make sure we always buy enough cans of paint.

## What I Learned

In this project, I practiced:

* Creating functions using `def`
* Passing arguments to functions
* Working with parameters
* Importing the `math` module
* Using `math.ceil()`
* Taking user input using `input()`
* Converting input using `int()`
* Performing mathematical calculations
* Using f-strings to display results

## Formula Used

First, the area of the wall is calculated:

```text
Wall Area = Height × Width
```

Then:

```text
Number of Cans = Wall Area / Coverage of One Can
```

Since we cannot normally buy a fraction of a paint can, the result is rounded **up**.

```python
math.ceil((height * width) / coverage)
```

## Code

```python
import math

def paint(height, width, coverage):
    no_of_cans = math.ceil((height * width) / coverage)

    print(f"You have to buy {no_of_cans} cans.")


height = int(input("Enter the height of the wall: "))
width = int(input("Enter the width of the wall: "))

coverage = 7

paint(height, width, coverage)
```

## How It Works

Suppose the user enters:

```text
Height = 5
Width = 8
```

The wall area is:

```text
5 × 8 = 40
```

One paint can covers:

```text
7 square units
```

Therefore:

```text
40 / 7 = 5.71
```

We can't rely on only 5 cans because they would not cover the entire wall.

So:

```python
math.ceil(5.71)
```

returns:

```text
6
```

The program displays:

```text
You have to buy 6 cans.
```

## Why `math.ceil()`?

`math.ceil()` rounds a number **up to the nearest integer**.

For example:

```python
math.ceil(5.1)   # 6
math.ceil(5.7)   # 6
math.ceil(6.0)   # 6
```

This is useful for the paint calculator because even if we need only a small part of another can, we still need to buy the whole can.

## Function Used

The main calculation is placed inside a function:

```python
def paint(height, width, coverage):
```

The function receives three values:

```text
height   → Height of the wall
width    → Width of the wall
coverage → Area covered by one paint can
```

It is called using:

```python
paint(height, width, coverage)
```

## Example Output

```text
Enter the height of the wall: 5
Enter the width of the wall: 8

You have to buy 6 cans.
```

Through this exercise, I practiced creating functions, passing arguments, using the `math` module, and applying `math.ceil()` to solve a practical problem.
