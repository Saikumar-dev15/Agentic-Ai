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
#mouse.eat()
#mouse.sleep()
#cat.Speak()
#mouse.Eat()



#Multiple inheritance = inherit from more than one parent class
#                       c(a, b)

#Multilevel inheritance = inherit from a parent which inherits from another parent
#                         c(b) <- b(a) <- a


class Animal:
    
    def __init__(self, name):
        self.name = name
        
        
    def eat(self):
        print(f" This {self.name} is eating")
        
    def sleep(self):
        print(f"This {self.name} is sleeping")
        
class prey(Animal):
    def flee(self):
        print("This {self.name} is fleeing")
        
class predator(Animal):
    def hunt(self):
        print("This {self.name} is hunting")
        
class Rabbit(prey):
    pass

class Hawk(predator):
    pass

class Fish(prey, predator):
    pass

rabbit = Rabbit("Moksha")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.eat()
rabbit.sleep()
#print(rabbit.flee())