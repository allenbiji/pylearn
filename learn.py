from random import shuffle

#create a guessing game

def shuffler(list):
    shuffle(list)
    return list

def guess():
    choice=input("enter your choice")
    return int(choice)

def guessgame(list,choice):
    if list[choice]=="0":
        print("correct guess")
    else:
        print("wrong")



list=[1,3,4,5,7,6,4]

shuffler(list)

a=guess()

guessgame(list,a)
print(list)