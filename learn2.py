class ShoppingCart:

    def __init__(self):
        self.list=[]

    def add_item(self,item,qty,price):
        return self.list.append((item,qty,price))

    def remove_item(self,item,qty):

    def __str__(self):
        return f'Shopping cart : {self.list}'



c=ShoppingCart()
c.add_item('a',20,30)
print(c)