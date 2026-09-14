import random
import HangManPics
import FruitNames
lives=6
print("---------Welcome to HangMan Game----------")
choosen_name=random.choice(FruitNames.fruits).lower()

display=[]
for i in range(len(choosen_name)):
    display.append('_')
print(display) 

gameover=False

while not gameover:
    guessed_letter=input("Guess a letter:").lower()
    for position in range(len(choosen_name)):
        letter = choosen_name[position]
        if(letter == guessed_letter):
            display[position]=guessed_letter
            print(display)
    if(guessed_letter not in choosen_name):
        lives-=1
        if(lives==0):
            gameover=True
            print("You lose,Game Over.")        
    if '_' not in display:
        gameover=True
        print("You won the game.")
    print(HangManPics.HANGMAN_PICS[lives])
    print(f"Only {lives} lives left.")
print(f"Your word is {choosen_name}.")    