class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True 
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")
        
class Dog(Animal):
    def Speak(self):
        print("Barks")
class Cat(Animal):
    def Speak(self):
        print("Meow!")

class Mouse(Animal):
    def Speak(self):
        print("Squeeks!...")
        
    def Eat(self):
        print("Chesse")

dog =Dog("Scobby")
cat =Cat("Tom")
mouse =Mouse("Jerry")

#print(mouse.name)
mouse.eat()
mouse.sleep()
cat.Speak()
mouse.Eat()