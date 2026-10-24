def add(num1: int , num2: int):
    return num1+num2

def subtract(num1: int , num2: int):
    return num1 - num2

def multiply(num1: int, num2: int):
    return num1 * num2 

def division(num1: int, num2: int):
    return num1/ num2


class BankAccount():
    def __init__(self, starting_balance=0):
        self.balance = starting_balance
        
    def deposite(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount

    def collect_invenstment(self):
        self.balance *= 1.1
        