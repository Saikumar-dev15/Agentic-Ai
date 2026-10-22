from app.calculation import add 

def test_add():
    print("testing add function")
    assert add(5,3) == 8
    