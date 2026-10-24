import pytest
from app.calculation import add, subtract, multiply, division , BankAccount

@pytest.mark.parametrize("num1, num2, expected", [
    (3,2, 5),
    (7,1, 8),
    (12,4, 16)
])

def test_add(num1, num2, expected):
    print("testing add function")
    assert add(num1 , num2) == expected
    
def test_subtract():
    assert subtract(9,4) == 5
    

def test_multiply():
    assert multiply(3,2) == 6
    
def test_division():
    assert division(8,4) == 2
    
    
def test_bank_set_initial_amount():
    bank_account = BankAccount(50)
    assert bank_account.balance == 50
    
def test_withdraw():
    bank_account = BankAccount(50)
    bank_account.withdrawal(20)
    assert bank_account.balance == 30
    

def test_deposite():
    bank_account = BankAccount(50)
    bank_account.deposite(50)
    assert bank_account.balance == 100