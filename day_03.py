student = {
    "name": "Umaira",                     
    "age": 22,
    "course": "Python",
    "marks": 90 } 
print(student)
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1:4])
print(numbers[:3])                   
print(numbers[2:5])
print(numbers[::2])
print(numbers[::-1])
student = {
    "name": "Umaira",
    "age": 22,
   "course": "Python"
}                                         
print(student.keys())
print(student.values()) 
print(student.items())
name = "Umaira"
course = "Python"
message = "Welcome to Python Learning"           
print(name)
print(course)
print(message) 
first_name = "Umaira"
last_name = "Shaik"                                 
full_name = first_name + " " + last_name
print(full_name)
word = "PYTHON"                          
print(word[::-1])
f = open("geek.txt", "r")
print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed)
f.close()
print("Is Closed?", f.closed)
file = open("geek.txt", "r")
content = file.read()
print(content)
file.close() 
with open("geek.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("File handling is easy with Python.")
print("File written successfully") 
try:
    number = int(input("Enter a number: "))
    print(100 / number)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Number cannot be zero")
try:
    a = 10
    b = 2
    result = a / b
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result:", result)
try:
    number = 10 / 2
    print(number)
except ZeroDivisionError:
    print("Error occurred")
finally:
    print("Program completed")
import math
print(math.sqrt(25))
print(math.factorial(5))
print(math.pi)








