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




#Exercise 

student = {
    "name" : "Sai",
    "Age"  : 19,
    "course" : "AARS"
}

try:
    key = input("Enter a Key: ")
    value = student[key]
    
    print("Value: ", value)
    
except KeyError:
    print("You Enter a Wrong Name Please verify...")
    
finally :
    print("Program completed")




#Exercise

Balance = 5000

try:
    amount = int(input("Enter a amount: "))
    if amount <= 0:
        print("Amount Should be greater than 0")
    
    elif amount > Balance:
        print("Invalid amount")
        
    else:
       Balance -= amount
       print("Withdrawed an amount : ", amount)
       print("Remaining Balance: ", Balance)
    
except ValueError:
    print("Invalid number. Suggested you to check Entered amount....")
      
finally:
    print("Transaction Completed..")
        