# 📅 Leap Year Checker

This is a simple Python program that checks whether a given year is a **leap year or not**.

The program uses nested `if` statements and the leap-year rules based on divisibility by **4, 100, and 400**.

## What I Learned

In this project, I practiced:

* Taking user input using `input()`
* Converting input using `int()`
* Using `if` and `else` statements
* Using nested conditional statements
* Using the modulus `%` operator
* Checking divisibility
* Implementing multiple conditions step by step

## Leap Year Rules

A year is a leap year when:

1. It is divisible by `4`.
2. If it is also divisible by `100`, then it must also be divisible by `400`.

In simple form:

```text
Divisible by 4?
      |
   ┌──┴──┐
   NO    YES
   |      |
Not Leap  Divisible by 100?
          |
       ┌──┴──┐
       NO    YES
       |      |
      Leap   Divisible by 400?
              |
           ┌──┴──┐
           NO    YES
           |      |
        Not Leap  Leap
```

## Code

```python
year = int(input("Enter the year: "))

if year % 4 == 0:

    if year % 100 == 0:

        if year % 400 == 0:
            print("It is a leap year.")

        else:
            print("It is not a leap year.")

    else:
        print("It is a leap year.")

else:
    print("It is not a leap year.")
```

## Understanding the Logic

### Rule 1 — Divisible by 4

```python
if year % 4 == 0:
```

If the remainder is `0`, the year is divisible by 4.

For example:

```text
2024 % 4 = 0
```

So `2024` can be a leap year.

### Rule 2 — Divisible by 100

Next, we check:

```python
if year % 100 == 0:
```

Years divisible by 100 require an additional check.

For example:

```text
1900 % 100 = 0
```

We cannot immediately say that `1900` is a leap year.

### Rule 3 — Divisible by 400

For century years, we check:

```python
if year % 400 == 0:
```

For example:

```text
2000 % 400 = 0
```

Therefore:

```text
2000 → Leap Year ✅
```

But:

```text
1900 % 400 != 0
```

Therefore:

```text
1900 → Not a Leap Year ❌
```

## Examples

| Year | Divisible by 4 | Divisible by 100 | Divisible by 400 | Result        |
| ---: | :------------: | :--------------: | :--------------: | ------------- |
| 2024 |        ✅       |         ❌        |         —        | Leap Year     |
| 2025 |        ❌       |         —        |         —        | Not Leap Year |
| 1900 |        ✅       |         ✅        |         ❌        | Not Leap Year |
| 2000 |        ✅       |         ✅        |         ✅        | Leap Year     |

## Example Output

```text
Enter the year: 2024
It is a leap year.
```

Another example:

```text
Enter the year: 1900
It is not a leap year.
```

## Why `%` is Used

The modulus operator `%` gives us the **remainder after division**.

For example:

```python
2024 % 4
```

returns:

```text
0
```

Therefore, `2024` is completely divisible by `4`.

But:

```python
2025 % 4
```

returns:

```text
1
```

so `2025` is not divisible by `4`.


Through this project, I practiced nested conditional statements, divisibility checks, and the modulus operator by implementing the rules used to determine whether a year is a leap year.
