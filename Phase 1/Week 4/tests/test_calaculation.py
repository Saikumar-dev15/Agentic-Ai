import pytest
from app.calculation import add, subtract, multiply, division , BankAccount


@pytest.fixture
def zero_bank_account():
    print("Creating empty bank account")
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)


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
    
    
def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50
    
def test_bank_default_amount(zero_bank_account):
    print("testing my bank account")
    assert  zero_bank_account.balance == 0
    
    
def test_withdraw(bank_account):
    bank_account.withdrawal(20)
    assert bank_account.balance == 30
    

def test_deposite(bank_account):
    bank_account.deposite(50)
    assert bank_account.balance == 100
    

def test_collect_intrest(bank_account):
    bank_account.collect_invenstment()
    assert round(bank_account.balance, 6) == 55
    
    
def test_bank_transcation(zero_bank_account):
    zero_bank_account.deposite(200)
    zero_bank_account.withdrawal(100)
    assert zero_bank_account.balance == 100