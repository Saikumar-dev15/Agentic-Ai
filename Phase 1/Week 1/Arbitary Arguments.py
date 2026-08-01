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


def largest(*args):
    Largest_num = args[0]
    
    for num in args:
        if num > Largest_num:
            Largest_num = num

#    print("Largest Number: ", num)
#print()
    
largest(3,5,7,8,9,2,10)



def Maxnumber(*args):
    Max_num = args[0]
    Min_num = args[0]
    
    for i in args:
        if i > Max_num:
            Max_number = i
         
        if i < Min_num:
            Min_num = i
            
    print("Largest Number: ", Max_number)
    print("Smallest Number: ", Min_num)
    
print()
Maxnumber(1,3,4,5,2,10,14)



def profile(**kwargs):
    for values in kwargs.values():
        print(values)
        
profile(name = "Sai",
        city = "Hyd",
        email = "kurapatilakshmisaikumar@gmail.com")


def Calculator(*args):
    total = 0
    Max_number = args[0]
    Min_number = args[0]
    
    for num in args:
        total += num
        
        if num in args:
            num> Max_number
            Max_number = num
            
        if num < Min_number:
            Min_number =num
            
    average = total/len(args)
    
    print("Sum : ", total)
    print("Average: ", average)
    print("Largest num ", Max_number)
    print("Smallest Num: ", Min_number)
    
Calculator(10,15,20,30)
