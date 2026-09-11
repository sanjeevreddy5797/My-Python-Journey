import random 

friends = ["Sanjeev" , "Kailash" , "Rupa" , "Karunkar" , "Viraaj" , "Joy"]

# 1st option to solve the problem 
number = random.randint(0,5)

print(f"{friends[number]} have to pay the bill.")

# 2nd option to solve the problem
print(f"{random.choice(friends)} have to pay the bill.")