values = [1,2,3,4,5,6]

#print("Hello", "World", values)

def sum(a,b,c):
    return a+b+c

#print(sum(1,2,3))

Values = [1,2,3,4,5,6]

v1,*v2,v3 = Values

#print(v1)                   #0 index
#print(v2)                   #1to4 index
#print(v3)                   # 5 index


list1 = [1,2,3]
list2 = [4,5,6]

combined = [*list1, "test", *list2]

#print(combined)



def my_print(name, age, job):
    print(f"{name} is {age} Years old and Works as a {job}")
   
#my_dict = {"name": "Sai", "age": 19, "job": "Programmer"} 
#my_print(**my_dict)

dict1 = {"name": "Sai", "age": 19, "job": "Programmer"} 
dict2 = {"Height": 185, "Weight": 60}

combined_dict = {**dict1, **dict2}

#print(combined_dict)



def my_function(**kwargs):
    print("The Following Parameters Were passed: ")
    
    for k,v in kwargs.items():
        print(f"Parameter Name: {k}, Parameter Value: {v}")
        
my_function(name="Priya", test="Hello", other="My World")