#Composition means building a class by putting objects of other classes inside it

class Engine:
    def start(self):
        print("Engine Started")
        
class Car:
    def __init__(self):
        self.engine = Engine()
        
    def start_car(self):
        self.engine.start()
        print("Car Started")
        
car = Car()
#car.start_car()    


#Exercise

class HelmetDetector:
    def detect(self):
        print("Detecting Helmet....")
    
class PlateOCR:
    def read_plate(self):
        print("Reading the Number Plate")
        
class Database:
    def save(self):
        print("Saving Violation")
        
#class HelmetSystem:
#    def __init__(self):
#        self.detector = HelmetDetector()
#        self.ocr = PlateOCR()
#        self.database = Database()
        
#    def process(self):
#        self.detector.detect()
#        self.ocr.read_plate()
#        self.database.save()
        
#system = HelmetSystem()
#system.process()
        
        
# Composition with constructor Arguments
class HelmetSystem:
    def __init__(self,detector,ocr,database):
        self.detector = detector
        self.ocr = ocr 
        self.database = database

    def process(self):
        self.detector.detect()
        self.ocr.read_plate()
        self.database.save()
        
detector = HelmetDetector()
ocr = PlateOCR()
database = Database()

#system = HelmetSystem(detector, ocr, database)
#system.process()


#Exercise 

class CPU:
    def info(self):
        print("CPU is Processing")
        
class RAM:
    def performance(self):
        print("RAM Loading......")
        
class Storage:
    def Capacity(self):
        print("Storage Storing Data....")

class Computer:
    def __init__(self,cpu, ram, storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        
    def run(self):
        self.cpu.info()
        self.ram.performance()
        self.storage.Capacity()

cpu = CPU()
ram = RAM()
storage = Storage()

computer = Computer(cpu, ram, storage)
#computer.run()




#Exercise

class Email:
    def send(self, message):
        print(f"Email Sent: {message}")
        
class SMS:
    def send(self, message):
        print(f"SMS Sent: {message}")
        
class NotificationSystem:
    def __init__(self, notification):
        self.notification = notification
        
    def notify(self, message):
        self.notification.send(message)
        
email = Email()
system = NotificationSystem(email)

system.notify(input("Enter the Information: "))


sms = SMS()
system = NotificationSystem(sms)

system.notify(input("Sent a msg: "))