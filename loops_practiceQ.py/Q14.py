#create a random no guessing game with python
import random
n=random.randint(1,11)
tries=0
while True:
    guess=int(input("enter a no:"))
    if n==guess:
        tries+=1
        print("you are right",tries)
        break
    elif n<guess:
        print("go a little lower")
        tries+=1
    elif n>guess:
        print("go little higher")
        tries+=1
    else:
        tries+=1
        print("you are wrong")