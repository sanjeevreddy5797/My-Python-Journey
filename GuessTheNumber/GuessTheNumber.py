import random
from art import logo

print(logo)

EASY_TURNS = 10
HARD_TURNS = 5

print("----------Welcome to the Number Guessing Game!----------")
print("I'm thinking of a number between 1 and 100")
number = random.randint(1,100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def no_of_lives():
              if difficulty == 'easy':
                     return EASY_TURNS
              elif difficulty == 'hard':
                     return HARD_TURNS



def game():
    attempts = no_of_lives()
    while attempts != 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guessed_number = int(input("Make a guess: "))
            if guessed_number == number:
                    print(f"You got it! The answer was {guessed_number}.")
                    return 
            elif guessed_number > number:
                    print("Too high.")
            else:                
                    print("Too low.")
                    
            attempts -=1

            if attempts > 1:
                    print("Guess Again.")       

    print("You've run out of guesses. Run the Game Again.")

game()