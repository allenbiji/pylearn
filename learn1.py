class Animal():

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self,breed):
        print(f'The name of the dog is {self.name}, he is {self.age} years old and his breed is {breed}')



dog=Animal("Jake",3)
dog.info("Pug")