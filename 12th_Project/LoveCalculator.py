name1=input("Enter your name:")
name2=input("Enter your love name:")
both_names=name1+name2
new_names=both_names.lower()
T=new_names.count('t')
R=new_names.count('r')
U=new_names.count('u')
E=new_names.count('e')
TRUE=T+R+U+E
L=new_names.count('l')
O=new_names.count('o')
V=new_names.count('v')
E=new_names.count('e')
LOVE=L+O+V+E
love_score=int(str(TRUE)+str(LOVE))
if(love_score<10 or love_score>90):
    print(f"Your love score is {love_score} and you will go like coke and mentos.")
elif(love_score>=40 and love_score<=50):
    print(f"Your love score is {love_score} and you are alright together.")
else:
    print(f"Your love score is {love_score}.")