def treasurepic():
    print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."   . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')

print("----------Welcome to Treasure Island----------")
print("----Your Mission is to find the treasure----")
direction = input("You're at a crossroad, where so you want to go? Type ('left' or 'right'): ").lower()

if(direction == 'left'):
    decision = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' for the boat or 'swim' to swim across lake: ").lower()
    if(decision == 'wait'):
        colour = input("You've crossed the lake , Which door that you want to select 'red','blue','yellow': ").lower()
        if(colour == 'yellow'):
            print("Hooreh!!! You won the Treasure...")
            treasurepic()  
        else:
            if(colour == 'red'):
                print("It's a room full of fire. Game Over.")
            elif(colour == "blue"):
                print("You enter into a room of beasts . Game Over.")
            else:
                print("Hooreh! You won the treasure...") 
                treasurepic()           
    else:
        print("You Were eaten by Crocodiles,Game Over.") 
else:
    print("OOPS! You Fell into hole,Game Over.")       