
# Define the Bookshop inventory as a dictionary
Bookshop = {'book1': 20, 'book2': 32, 'book3': 2, 'book4': 2}

class Sales:
    def __init__(self, name):
        self.name = name

    def buy(self, quantity):
        if self.name in Bookshop:
            Bookshop[self.name] += quantity
            return f'New quantity of {self.name} is {Bookshop[self.name]}'
        else:
            return f'Book {self.name} not found in inventory'

# Example usage
# Initialize a Sales object for a specific book
a = Sales('book1')

# Buy 3 more of 'book1'
print(a.buy(3))  # Output: New quantity of book1 is 23

# Initialize a Sales object for a non-existent book
b = Sales('book5')
print(b.buy(3))  # Output: Book book5 not found in inventory
