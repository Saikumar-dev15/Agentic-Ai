class Car:
    wheels = 4
    
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
    def drive(self):
        print(f"You drive the car {self.model}{self.year}")
    
    def Attributes(self):
        print(f"Your car contains {self.model} model and {self.color}")
    
    def describe(self):
        print(self.model, self.color)
    
car1 = Car("Mustang", 2024, "red", False)

#car1.describe()




class Employee():
    company = "Tata"
    
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def dispaly(self):
        print(f"Employee Name = {self.name} & ID = {self.id}")
        
    def annualsalary(self):
        annualsalary = self.salary * 10
        print(annualsalary)


employee = Employee("Sai", "TATA52716", 40000)

#employee.annualsalary()
#employee.dispaly()

#print(f"Company Name = {Employee.company}")



class BookLibrary():
    def __init__(self, author, title, price):
        self.author = author
        self.title = title
        self.price = price

    def display(self):
        print(f"The Title of the Book is {self.title}")
        print(f"Author of the Book is {self.author}")
        
    def Cost(self):
        print(f"The cost of the Book is {self.price}")
        if self.price >= 1000:
            discount_price = self.price * 0.90
            print(discount_price)
        

Book = BookLibrary("Meher Nolan", "Sakthi", 1500)

#Book.Cost()
#Book.display()


class Hospital():
    hospital_name = "Kameneni"
    patient_count = 0
    
    def __init__(self, patient_name, disease, age):
        self.patient_name = patient_name
        self.disease = disease
        self.age = age
        
        Hospital.patient_count +=1
        
    def display(self):
        print(f"Name of the Patient = {self.patient_name}")
        print(f"Disease = {self.disease}")
        print(f"Age of the patient = {self.age}")
        
        
    def Discharge(self):
        Hospital.patient_count -= 1
        print(self.patient_name , "has been discharged.")
        print(f"Hospital Discharge count = {Hospital.patient_count}")
        
    def admitted(self):
        print(f"{self.patient_name} Was Admitted in {Hospital.hospital_name}")
        print(f"Current Admited count = {Hospital.patient_count}")
        
        
        

p1 = Hospital("Gowtham", "rabbies", 20)
p2 = Hospital("Mohit", "HIV", 20)
p3 = Hospital("Greshmant", "Diabetic", 20)
p4 = Hospital("Shiva" , "comma", 22 )

#print(Hospital.patient_count)
p2.Discharge()
p5 = Hospital("Varun" , "Milk Donation", 22)
p5.admitted()

print(f"Total Count of Patients: {Hospital.patient_count}")