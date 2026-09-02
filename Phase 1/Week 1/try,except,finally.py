try:
    number = int(input("Enter a number: "))
    print(number)
    
except ValueError:
    print("Invalid input")
    
finally:
    print("Peogram finished")
    
    
try:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: ")) 
    
    results = num1/num2
    
    print(f"Results: {results}")   
    
except ValueError:
    print("Invalid input")
    
except ZeroDivisionError:
    print("Cannot divided by Zero...")
    
finally:
    print("You are Accesed to see your Results!....")