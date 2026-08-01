# List comprehension = Aconcise to create lists in python.
#                      Compact and Easier to read than traditional loops
#                      [expression for value in iterable if condition]


#Manual Way
x = []
for i in range (1,11):
    x.append(i*2)
    
#print(x)



#List Comprehension Method

x = [x*2 for x in range(1,11)]
#print(x)

numbers = [1 ,2, 3, -2, -6, -10]
positive_numbers = [num for num in numbers if num>=0]
negative_numbers = [ num for num in numbers if num<= 0]
even_numbers = [ num for num in numbers if num%2 == 0]
#print(even_numbers)

grades = [85, 42, 79 , 98, 56, 61, 31]
passing_grades = [grade for grade in grades if grade>=40]
#print(passing_grades)




# Silcing 
import numpy as np 

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

#array[start:end:step]

print(array[::-2])  
print(array[:, 0:2])     
print(array[:, ::2])  
print(array[:, 1::2])    
 
print(array[0:2, 2:])                     #Row and Coloumns
print(array[2: , 0:2])                      # [9,10] and [13,14]
print(array[2: , 2:])                        #[11,12] and [15,16]
