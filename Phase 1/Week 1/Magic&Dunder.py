class Author:
    def __init__(self, name, book_name, pages):
        self.name = name
        self.book_name = book_name
        self.pages = pages
        
    
    def __str__(self):
        return f"{self.book_name} by {self.name}"
    
    def __len__(self):
        return self.pages
    
    def __call__(self, *args, **kwargd):
        print("Hi")
    
#    def __del__(self):
#        print("Author has been Deleted")
    
d = Author("Nolan", "The Odeseey", 300)\
    
#print(d)
#print(len(d))





class BankAccount():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance
    
    def __sub__(self,other):
        return self.balance - other.balance
    
    def __mul__(self, other):
        return self.balance * other.balance
    
    def __truediv__(self, other):
        return self.balance / other.balance
    
    
acc1 = BankAccount("Sai", 500000)
acc2 = BankAccount("Priya", 10000)


#print(acc1 + acc2)
#print(acc1-acc2)
#print(acc1 * acc2)
#print(acc1 / acc2)



class Laptop():
    def __init__(self, brand, ram):
        self.ram = ram
        self.brand = ram

    def __eq__(self, other):
        if not isinstance(other, Laptop):
            return NotImplemented
        
        return self.ram == other.ram
       
laptop1 = Laptop("Dell", 16)
laptop2 = Laptop("Asus", 32)
laptop3 = Laptop("Lenova", 8)

#print(laptop1 == laptop2)
#print(laptop2 == laptop3)
