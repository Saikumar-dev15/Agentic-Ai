#ARBITRARY ARGUMENTS
# *args = allows you to pass multiple non-key  arguments
# **kwargs = allow you to pass multiple keyword- arguments

def add(*args):
    total =0 
    for arg in args:
        total += arg
    return total
#print(add(1,2,4,5))

#def display_name(*args):
#    for arg in args:
#        print(arg, end=" ")
    
#    print()

#display_name("Mr.", "Sai", "Kumar", "Choudary")


# **kwargs
#def print_address(**kwargs):
#        for value in kwargs.values():
#            print(value)
            
#print_address(street="123 fake st.",
#              city="Hydrabad",
#              state="Telangana",
#              pincode="508218")




#exercise on both *args and **kwargs
def shipping_label(*args, **kwargs):
    for arg in args:
       print(arg, end=" ")
    
    print()
    
    for value in kwargs.values():
       print(value, end=" ")
    
shipping_label("Mr.", "Sai", "Kumar", "Choudary",
               street="123 fake st.",
               city="Hydrabad",
               state="Telangana",
               pincode="508218")



def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
#print()
#print(add(20,30,50))



def largest_num(*args):
       print("Largest Number: ", max(args))
    
#largest_num(2,5,7,3,8)

