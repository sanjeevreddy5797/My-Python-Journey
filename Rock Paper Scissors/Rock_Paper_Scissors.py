import random
import RPS_Module

user_choice=int(input("Enter the number '0 for rock','1 for paper' and '2 for scissors:"))
computer_choice=random.randint(0,2)

if(user_choice>=3 and user_choice<0):
    print("Input is invalid,try again!")
else:
    if(user_choice==computer_choice):
        print(f"Computer choice : \n{RPS_Module.list1[computer_choice]}")
        print(f"your choice : \n {RPS_Module.list1[user_choice]}")
        print("It's a draw ! ! !")
    elif(computer_choice==0 and user_choice==2):
         print(f"Computer choice : \n{RPS_Module.list1[computer_choice]}")
         print(f"your choice : \n {RPS_Module.list1[user_choice]}")
         print("You lose ! ! !")
    elif(user_choice==0 and computer_choice==2):
        print(f"Computer choice : \n{RPS_Module.list1[computer_choice]}")
        print(f"your choice : \n {RPS_Module.list1[user_choice]}")
        print("You win ! ! !")
    elif(computer_choice>user_choice):
        print(f"! ! !omputer choice : \n{RPS_Module.list1[computer_choice]}")
        print(f"your choice : \n {RPS_Module.list1[user_choice]}")
        print("You lost ! ! !")
    elif(computer_choice<user_choice):
         print(f"Computer choice : \n{RPS_Module.list1[computer_choice]}")
         print(f"your choice : \n {RPS_Module.list1[user_choice]}")
         print("You win ! ! !")