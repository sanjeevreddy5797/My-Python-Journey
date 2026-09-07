print("----------Welcome to the Tip Calculator----------\n")
bill = int(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10,12, or 15?"))
no_of_people = int(input("How many people to split the bill?"))

# total tip calculation
total_tip = (bill / 100) * tip

# total bill calculation including tip
total_bill = bill + total_tip

# total bill per each person
bill_per_person = total_bill / no_of_people

# output
print(f"The total bill per person is {round(bill_per_person,2)} ")