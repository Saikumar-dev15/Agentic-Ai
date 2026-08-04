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
    
    def __del__(self):
        print("Author has been Deleted")
    
d = Author("Nolan", "The Odeseey", 300)\
    
print(d)
print(len(d))
d()
del d

