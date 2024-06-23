import random


n=random.randint(1,100)

while True:
    inp=int(input("Enter no."))
    if inp==n:
        print("you chose the correct no.")
        break
    else:
        print("wrong guess, try again")
        continue
