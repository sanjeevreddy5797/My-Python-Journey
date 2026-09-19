# 🧮 Python Calculator

This is a simple **command-line calculator** built using Python.

The calculator performs basic mathematical operations and allows the user to continue calculations using the previous result or start a completely new calculation.

## What I Learned

In this project, I practiced:

* Creating functions using `def`
* Using parameters and return values
* Storing functions inside a dictionary
* Calling functions using dictionary values
* Using `while` loops
* Using `for` loops
* Using conditional statements
* Working with floating-point numbers
* Using f-strings
* Importing a custom module
* Reusing the result of a previous calculation

## Supported Operations

The calculator supports:

| Symbol | Operation      |
| ------ | -------------- |
| `+`    | Addition       |
| `-`    | Subtraction    |
| `*`    | Multiplication |
| `/`    | Division       |

## Project Structure

```text
Calculator/
│
├── main.py
└── logo.py
```

`main.py` contains the calculator logic, while `logo.py` contains the ASCII-art calculator logo.

## Calculator Functions

Each mathematical operation has its own function.

```python
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
```

For example:

```python
add(10, 5)
```

returns:

```text
15
```

## Operations Dictionary

The functions are stored inside a dictionary:

```python
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
```

Here:

```text
"+" → add()
"-" → subtract()
"*" → multiply()
"/" → divide()
```

This allows the program to select a function based on the operation entered by the user.

## Complete Code

```python
import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():

    print(logo.logo)

    number1 = float(input("What's the first number?: "))

    condition = True

    while condition:

        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")

        number2 = float(input("What is the second number?: "))

        result = operations[operation_symbol](number1, number2)

        print(f"{number1} {operation_symbol} {number2} = {result}")

        continue_calculation = input(
            f"Type 'y' to continue calculating with {result}, "
            "or type 'n' to start a new calculation: "
        )

        if continue_calculation == 'y':
            number1 = result

        else:
            condition = False
            print("\n" * 20)
            calculator()


calculator()
```

## How the Calculator Works

The program first asks for the first number:

```text
What's the first number?: 10
```

It then displays the available operations:

```text
+
-
*
/
```

The user selects an operation:

```text
Pick an operation: +
```

and enters the second number:

```text
What is the second number?: 5
```

The program calculates:

```text
10 + 5 = 15
```

## Calling Functions from a Dictionary

One of the most important lines in this project is:

```python
result = operations[operation_symbol](number1, number2)
```

Suppose:

```python
operation_symbol = "+"
```

Python first evaluates:

```python
operations["+"]
```

The dictionary contains:

```python
"+": add
```

So it gets the `add` function.

Therefore:

```python
operations["+"](10, 5)
```

becomes:

```python
add(10, 5)
```

and returns:

```text
15
```

So the flow is:

```text
operations["+"](10, 5)
        ↓
     add(10, 5)
        ↓
       15
```

This project helped me understand that **functions can be stored as values inside Python dictionaries**.

## Continuing a Calculation

After calculating a result, the program asks:

```text
Type 'y' to continue calculating with 15.0,
or type 'n' to start a new calculation:
```

If the user enters:

```text
y
```

the previous result becomes the first number:

```python
number1 = result
```

For example:

```text
10 + 5 = 15

Continue with 15?

15 * 2 = 30

Continue with 30?

30 - 10 = 20
```

This allows calculations to be chained together.

## Example Output

```text
What's the first number?: 10

+
-
*
/

Pick an operation: +
What is the second number?: 5

10.0 + 5.0 = 15.0

Type 'y' to continue calculating with 15.0,
or type 'n' to start a new calculation: y

+
-
*
/

Pick an operation: *

What is the second number?: 3

15.0 * 3.0 = 45.0
```

## Program Flow

```text
START
  ↓
Display Calculator Logo
  ↓
Enter First Number
  ↓
Choose Operation
  ↓
Enter Second Number
  ↓
Perform Calculation
  ↓
Display Result
  ↓
Continue with Result?
   /            \
 YES             NO
  ↓               ↓
Use result      Start New
as number1      Calculation
  ↓               ↓
Calculate       calculator()
Again
```

## Corrections Made

### Displaying the Logo

Instead of:

```python
logo.logo
```

the program uses:

```python
print(logo.logo)
```

so the logo is actually displayed.

### Showing the Result in the Input Message

Instead of:

```python
input("Continue calculating with {result}")
```

an f-string is used:

```python
input(f"Continue calculating with {result}")
```

so the actual result appears.

For example:

```text
Continue calculating with 15.0
```

instead of:

```text
Continue calculating with {result}
```

## Possible Future Improvements 🚀

As I learn more Python, I can improve the calculator by:

* Handling division by zero
* Handling invalid operation symbols
* Handling non-numeric input
* Avoiding recursive calls when starting a new calculation
* Adding operations such as `%`, powers, and square roots
* Adding an exit option
* Improving the calculator interface

Through this project, I practiced functions, dictionaries, loops, return values, custom modules, and dynamic function calls while building an interactive calculator.           

