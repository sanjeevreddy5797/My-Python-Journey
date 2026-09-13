import math

def paint(height,width,coverage):

    no_of_cans=math.ceil((height*width)/coverage)
    print(f"You have to buy {no_of_cans} of cans.")


height=int(input("Enter the height of the wall:"))

width=int(input("Enter the width of the wall:"))

coverage=7

paint(height,width,coverage)