print("----------Welcome to Prime Number Checker-----------")
def is_prime(number):
    count = 0 
    for i in range(1,number + 1):
        if number % i == 0:
            count += 1

    if number == 1:
        print(f"{number} is neither Prime nor Composite Number.")
    elif count <= 2:
        print(f"{number} is a Prime Number.")
    else:
        print(f"{number} is not a Prime Number.")

is_prime(int(input("Enter the number that you want to know either it is Prime or Not: ")))