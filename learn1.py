class Animal():

    def __init__(self):
        print("Animal Created")

    def eat(self):
        print("Our dog is eating")

    def __str__(self):
        return f'This is the animal class'

animal=Animal()
animal.eat()
print(animal)