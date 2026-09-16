# 🔨 Silent Auction Program

This is a simple **Silent Auction program built using Python**.

The program allows multiple people to enter their names and bid amounts. After everyone has finished bidding, the program finds the person with the **highest bid** and announces the winner.

## What I Learned

In this project, I practiced:

* Creating Python dictionaries
* Adding key-value pairs to dictionaries
* Using `while` loops
* Taking user input
* Using Boolean variables
* Using `.lower()`
* Using `max()`
* Using `.values()`
* Using `dict.get`
* Importing a custom Python module
* Finding the maximum value and its corresponding key

## Project Structure

```text
Silent-Auction/
│
├── main.py
└── artLogo.py
```

### `main.py`

Contains the main auction logic.

### `artLogo.py`

Contains the ASCII-art logo displayed when the program starts.

The logo is imported using:

```python
import artLogo
```

and displayed using:

```python
print(artLogo.logo)
```

## How the Program Works

The program starts with an empty dictionary:

```python
bids = {}
```

Every bidder enters their name and bid:

```python
name = input("What is your name? : ")
price = int(input("What is your bid?: $"))
```

The information is stored in the dictionary:

```python
bids[name] = price
```

For example, after three people bid:

```python
bids = {
    "Sanjeev": 150,
    "Kailash": 200,
    "Joy": 175
}
```

Here:

```text
KEY          VALUE

Sanjeev  →   150
Kailash  →   200
Joy      →   175
```

The bidder's **name is the key**, and the **bid amount is the value**.

## Finding the Highest Bid

The highest bid is found using:

```python
highest_bid = max(bids.values())
```

For:

```python
bids = {
    "Sanjeev": 150,
    "Kailash": 200,
    "Joy": 175
}
```

`bids.values()` gives the bid amounts:

```text
150, 200, 175
```

and:

```python
max(bids.values())
```

returns:

```text
200
```

## Finding the Winner

The winner's name is found using:

```python
winner_name = max(bids, key=bids.get)
```

This tells Python:

> Look through the keys in `bids`, but compare them based on their corresponding values.

For example:

```text
Sanjeev  → 150
Kailash  → 200  ← Highest
Joy      → 175
```

Therefore:

```python
winner_name = "Kailash"
```

and:

```python
highest_bid = 200
```

The program displays:

```text
The winner is Kailash with a bid of $200.
```

## Complete Code

```python
import artLogo

print(artLogo.logo)

print("----------Welcome to the Silent Auction----------")

bids = {}

continue_bidding = True

while continue_bidding:

    name = input("What is your name? : ")

    price = int(input("What is your bid?: $"))

    bids[name] = price

    should_continue = input(
        "Anyone here to bid more? "
        "Type 'yes' if you are interested, "
        "Type 'no' if you are not: "
    ).lower()

    if should_continue == 'yes':

        continue_bidding = True

    else:

        continue_bidding = False

        highest_bid = max(bids.values())

        winner_name = max(bids, key=bids.get)

        print(
            f"The winner is {winner_name} "
            f"with a bid of ${highest_bid}."
        )
```

## Program Flow

```text
START
  ↓
Display Auction Logo
  ↓
Create Empty Dictionary
  ↓
Enter Bidder Name
  ↓
Enter Bid Amount
  ↓
Store Name → Bid
  ↓
More Bidders?
   /      \
 YES       NO
  ↓         ↓
Repeat    Find Highest Bid
            ↓
         Find Winner
            ↓
      Announce Winner 🏆
```

## Example

```text
----------Welcome to the Silent Auction----------

What is your name? : Sanjeev
What is your bid?: $150

Anyone here to bid more?
yes

What is your name? : Kailash
What is your bid?: $250

Anyone here to bid more?
yes

What is your name? : Joy
What is your bid?: $180

Anyone here to bid more?
no

The winner is Kailash with a bid of $250.
```

## Important Concept — `max(bids, key=bids.get)`

One of the most important lines I learned in this project is:

```python
winner_name = max(bids, key=bids.get)
```

Normally:

```python
max(bids)
```

would compare the dictionary's **keys**.

But:

```python
max(bids, key=bids.get)
```

uses each key's associated **value** for comparison.

So if:

```python
bids = {
    "Sanjeev": 150,
    "Kailash": 250,
    "Joy": 180
}
```

Python effectively compares:

```text
Sanjeev → bids.get("Sanjeev") → 150
Kailash → bids.get("Kailash") → 250
Joy     → bids.get("Joy")     → 180
```

The largest value is `250`, so the corresponding key `"Kailash"` is returned.

## Future Improvements 🚀

As I learn more Python, I can improve this project by:

* Hiding previous bidders' information between turns
* Handling invalid bid amounts
* Preventing empty names
* Handling multiple bidders with the same highest bid
* Moving the winner calculation into a function
* Allowing the auction to restart

Through this project, I practiced dictionaries, loops, user input, custom modules, and learned how to find both the maximum value and its corresponding key in a Python dictionary.