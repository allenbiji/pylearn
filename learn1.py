class Animal():

    def __init__(self):
        print("Animal Created")

    def eat():
        print("Our dog is eating")

class Dog(Animal):
     def __init__(self):
         Animal.__init__()
         print("Dog says hi")


Dog.eat()