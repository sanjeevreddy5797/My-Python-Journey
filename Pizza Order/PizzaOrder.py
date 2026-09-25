print("----------Welcome to Python Pizza Deliveries----------")

#input to take the size of the pizza

size = input("What size do you want? S, M or L: ")

#asking user that he/she needs pepperoni or not

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")

#asking user that he/she needs extra cheese or not

extra_cheese = input("Do you want cheese on your pizza? Y or N: ")

total_bill=0


if (size == 'S' or size== 's'):
    total_bill += 15
elif (size == 'M' or size == 'm'):
    total_bill += 20
elif (size == 'L' or size == 'l'):
    total_bill += 25
else:
    print("! ! ! Please select the Appropriate size.")


if(pepperoni == 'Y' or pepperoni == 'y'):
    if(size == 'S' or size == 's'):
        total_bill+=2
    else:
        total_bill+=3    

if(extra_cheese == 'Y' or extra_cheese == 'y'):
    total_bill+=1

#output

print(f"Your Total bill is ${total_bill}.")