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




class Player():
    def __init__(self,name, score):
        self.name = name
        self.score = score
        

    def __lt__(self, other):
        return self.score < other.score
    
p1 =Player("Sai Kumar", 7)
p2 =Player("Mohit", 18)
p3 = Player("Gowtham", 45)
p4 = Player("Grishmant", 99)

#print(p1 < p2)
#print(p1 > p3)
#print(p1 > p4)




class Movielist():
    def __init__(self):
        self.movies = ["RRR", "Bahubali", "Devara", "Salaar"]
        
    def __getitem__(self, index):
        return self.movies[index]
        
    def __setitem__(self, index, value):
        self.movies[index] = value
        
    def __contains__(self, movies):
        return movies in self.movies
    
    
M = Movielist()
M[1] = "Bahubali 2"
print(M[3])
print(M.movies)
print("OG" in Movielist)
print("Devara" in Movielist)


