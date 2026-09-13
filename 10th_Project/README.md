# 🎨 Paint Area Calculator

This is a simple Python program that calculates the **number of paint cans required to paint a wall** based on the wall's height and width in feet.

In this project, one paint can is assumed to cover **7 square feet**.

## What I Learned

In this project, I practiced:

* Creating functions using `def`
* Passing arguments to functions
* Taking user input using `input()`
* Converting input using `int()`
* Importing and using the `math` module
* Using `math.ceil()`
* Performing calculations inside a function
* Solving a simple real-world problem using Python

## Formula Used

First, the area of the wall is calculated:

```text
Wall Area = Height × Width
```

Since height and width are entered in feet:

```text
Wall Area = square feet (ft²)
```

Then the number of paint cans required is:

```text
Number of Cans = Wall Area / Coverage per Can
```

In this program:

```text
Coverage per Can = 7 ft²
```

## Code

```python
import math

def paint(height, width, coverage):

    no_of_cans = math.ceil((height * width) / coverage)

    print(f"You have to buy {no_of_cans} cans.")


height = int(input("Enter the height of the wall in feet: "))

width = int(input("Enter the width of the wall in feet: "))

coverage = 7

paint(height, width, coverage)
```

## Example

Suppose the user enters:

```text
Height = 6 feet
Width = 8 feet
```

The area of the wall is:

```text
6 × 8 = 48 ft²
```

Each paint can covers:

```text
7 ft²
```

Therefore:

```text
48 / 7 = 6.857...
```

Using:

```python
math.ceil(6.857)
```

we get:

```text
7
```

So the output is:

```text
You have to buy 7 cans.
```

## Why `math.ceil()`?

We use:

```python
math.ceil()
```

because the number of cans must be rounded **up**.

For example, if the calculation says:

```text
6.2 cans
```

we cannot buy only `0.2` of another can, so we need:

```text
7 cans
```

## Function Used

The calculation is performed inside:

```python
def paint(height, width, coverage):
```

The function receives three parameters:

* `height` → Height of the wall in feet
* `width` → Width of the wall in feet
* `coverage` → Area one paint can can cover

The function is called using:

```python
paint(height, width, coverage)
```

## Example Output

```text
Enter the height of the wall in feet: 6
Enter the width of the wall in feet: 8

You have to buy 7 cans.
```

Through this project, I practiced Python functions, parameters, mathematical calculations, and the `math.ceil()` function by building a simple paint area calculator.
