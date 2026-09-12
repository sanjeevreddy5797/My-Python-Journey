import random
numbers = ['0','1','2','3','4','5','6','7','8','9']
characters = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+',
    '[', ']', '{', '}',
    ';', ':', "'", '"',
    ',', '<', '.', '>',
    '/', '?', '\\', '|'
]
words = [
    'a','b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J',
    'K','L','M','N','O','P','Q','R','S','T',
    'U','V','W','X','Y','Z'
]
print("----------Welcome to the password generator----------")
n_numbers=int(input("Enter the no of numbers you want to have in your password:"))
n_characters=int(input("Enter the no of characters you want to have in your password:"))
n_words=int(input("Enter the no of words you want to have in your password:"))
password=[]
for i in range(0,n_numbers):
    password.append(random.choice(numbers))
for i in range(0,n_characters):
    password.append(random.choice(characters))
for i in range(0,n_words):
    password.append(random.choice(words))
random.shuffle(password) 

new_password=''
for i in range(len(password)):
    new_password+=password[i]
print(f"Your Password is {new_password}")
