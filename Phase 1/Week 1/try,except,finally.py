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
        
        
        

#Custom Exception

class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

        super().__init__(
            f"Balance: {balance}, Withdrawal: {amount}"
        )
        
try:
    balance = 5000
    amount  = 7000
    
    if amount > balance:
        raise InsufficientBalanceError(balance, amount)
    
except InsufficientBalanceError as e:
    print(e)






#Multiple Custom Exceptions

class InvalidAgeError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

try:
    age = int(input("Enter your Age: "))
    amount = int(input("Enter a amount: "))
    
    balance = 15000
    
    if age <= 18:
        raise InvalidAgeError("You are not eligible to access. You must be 18 or older to get access")
    
    if amount <= 0 :
        raise InvalidAmountError("you should enter greater than 0 amount. 0 is not withdrawal amount.")
    
    elif amount > balance:
        raise InsufficientBalanceError("Please check the entered amount.")
    
    else :
        balance -= amount
        print(f"Withdrawal amount : {amount}")
        print(f"Remaining Balance : {balance}")
    print("Succesfully Withdrawal...")
    
except ValueError:
    print("Invalid amount.")
    
except InvalidAgeError as e:
    print(e)
    
except InvalidAmountError as e:
    print(e)
    
except InsufficientBalanceError as e:
    print(e)
    
    
