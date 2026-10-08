# 🔐 Caesar Cipher

This is a simple **Caesar Cipher encryption and decryption program** built using Python.

The program allows the user to enter a message and a shift number. Each letter in the message is shifted through the alphabet to produce an encrypted message.

The same program can also decrypt the encrypted message using the original shift number.

## What I Learned

In this project, I practiced:

* Using `while` loops
* Using `for` loops
* Using `if`, `elif`, and `else`
* Working with strings character by character
* Using `ord()` to get the numeric value of a character
* Using `chr()` to convert a numeric value back into a character
* Using the modulo `%` operator
* Implementing encryption and decryption
* Preserving spaces in a message
* Allowing the program to run multiple times

## What is a Caesar Cipher?

A Caesar Cipher is a simple substitution cipher where each letter is shifted by a fixed number of positions in the alphabet.

For example, with a shift of `3`:

```text id="p17z0j"
a → d
b → e
c → f
d → g
```

So:

```text id="bnkmcz"
hello
```

becomes:

```text id="fd1w6s"
khoor
```

## Encryption

The program encrypts each character using:

```python id="e92ot3"
new_char = chr((ord(ch) - 97 + shift_number) % 26 + 97)
```

For example, if:

```text id="f54jhw"
ch = 'a'
shift = 3
```

then:

```text id="at5zrw"
ord('a') = 97

97 - 97 = 0

0 + 3 = 3

3 % 26 = 3

3 + 97 = 100

chr(100) = 'd'
```

Therefore:

```text id="s08fpx"
a → d
```

## Why `% 26`?

The English alphabet contains **26 letters**.

Modulo allows the program to wrap around when it reaches the end of the alphabet.

For example, with a shift of `3`:

```text id="zzk67y"
x → a
y → b
z → c
```

Without `% 26`, the program would continue to other character codes instead of returning to `a`.

## Decryption

Decryption uses the opposite operation:

```python id="ybzhy5"
new_char = chr((ord(ch) - 97 - shift_number) % 26 + 97)
```

Encryption:

```text id="umctam"
+ shift
```

Decryption:

```text id="fybxl6"
- shift
```

For example:

```text id="o6a0lr"
Original  → hello

Encrypt
shift 3
    ↓
khoor

Decrypt
shift 3
    ↓
hello
```

## Handling Spaces

The program keeps spaces unchanged:

```python id="aw5x9e"
if ch == " ":
    encrypted_message += ch
```

Therefore:

```text id="ppq2k5"
hello world
```

with a shift of `3` becomes:

```text id="cct7f4"
khoor zruog
```

instead of trying to encrypt the space.

## Complete Code

```python id="ijxl0j"
print("----------Welcome to Caesar Cipher----------")

condition = True

while condition:

    en_or_de = input(
        "Type 'encrypt' for encryption, "
        "type 'decrypt' for decryption:"
    )

    if en_or_de == "encrypt":

        message = input("Type your message:")
        shift_number = int(input("Type the shift number:"))

        encrypted_message = ""

        for ch in message:

            if ch == " ":
                encrypted_message += ch

            else:
                new_char = chr(
                    (ord(ch) - 97 + shift_number) % 26 + 97
                )

                encrypted_message += new_char

        print(
            f"Here is the text after encryption:"
            f"{encrypted_message}"
        )

    elif en_or_de == "decrypt":

        message = input("Type your message:")
        shift_number = int(input("Type the shift number:"))

        decrypted_message = ""

        for ch in message:

            if ch == " ":
                decrypted_message += ch

            else:
                new_char = chr(
                    (ord(ch) - 97 - shift_number) % 26 + 97
                )

                decrypted_message += new_char

        print(
            f"Here is the text after decryption:"
            f"{decrypted_message}"
        )

    condition1 = input(
        "Type 'yes' if you want to go again. "
        "Otherwise type 'no': "
    )

    if condition1 == "yes":
        condition = True

    else:
        condition = False
        print("Good Bye.")
```

## Program Flow

```text id="usj8qd"
START
  ↓
Encrypt or Decrypt?
  ↓
Enter Message
  ↓
Enter Shift Number
  ↓
┌─────────────────────┐
│                     │
Encrypt             Decrypt
   │                    │
+ Shift              - Shift
   │                    │
└─────────┬───────────┘
          ↓
    Process Letters
          ↓
    Display Result
          ↓
      Go Again?
       /     \
     Yes      No
      ↓        ↓
   Restart   Goodbye
```

## Example - Encryption

```text id="w9cvvr"
----------Welcome to Caesar Cipher----------

Type 'encrypt' for encryption, type 'decrypt' for decryption:
encrypt

Type your message:
hello world

Type the shift number:
3

Here is the text after encryption:
khoor zruog
```

## Example - Decryption

Using the encrypted message:

```text id="m1s4cv"
khoor zruog
```

with the same shift:

```text id="e0j97g"
3
```

produces:

```text id="xunm6v"
hello world
```

## Important Python Functions

### `ord()`

`ord()` converts a character into its Unicode code point.

```python id="94w5d3"
ord('a')
```

returns:

```text id="5emdyh"
97
```

### `chr()`

`chr()` performs the opposite operation.

```python id="6wwa3e"
chr(97)
```

returns:

```text id="qct1fd"
a
```

Together, `ord()` and `chr()` allow the program to mathematically shift letters.

## Current Limitation

This version is designed primarily for **lowercase English letters and spaces**.

For example:

```text id="okd8xs"
hello world
```

works correctly.

Uppercase letters, numbers, punctuation, and other symbols are not currently handled correctly by the cipher logic.

This can be improved later by checking whether each character is an alphabetic lowercase letter before shifting it.

Through this project, I practiced loops, conditional statements, string manipulation, ASCII/Unicode character conversion, modulo arithmetic, and basic encryption/decryption logic by implementing the Caesar Cipher.
