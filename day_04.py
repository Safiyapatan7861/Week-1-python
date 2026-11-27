def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print(add(10, 20))
print(subtract(20, 10))

import math
print(math.sqrt(25))
from mypackage.addition import add
from mypackage.subtraction import subtract
print(add(10, 20))
print(subtract(20, 10))

from math import sqrt
print(sqrt(36))

class Student:
    name = "Umaira"
    age = 22
print(Student.name)
print(Student.age)

class Student:
    name = "Umaira"
    age = 22
student1 = Student()
print(student1.name)
print(student1.age)  

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = Student("Umaira", 22)
print(student1.name)
print(student1.age)
class Student:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Student name:", self.name)
student1 = Student("Umaira")
student1.display()
class Student:
    school = "ABC School"  # Class variable
    def __init__(self, name, age):
        self.name = name   # Instance variable
        self.age = age
student1 = Student("Umaira", 22)
student2 = Student("Aisha", 21)
print(student1.name)
print(student2.name)
print(student1.school)
print(student2.school)
class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
dog1 = Dog()
dog1.eat()
dog1.bark()
class Dog:
    def sound(self):
        print("Dog barks")
class Cat:
    def sound(self):
        print("Cat meows")
dog = Dog()
cat = Cat()
dog.sound()
cat.sound()

class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)

account = Bank(5000)

account.show_balance()

class Student:

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)

    def result(self):
        if self.marks >= 25:
            print("Result: Pass")
        else:
            print("Result: Fail")


student1 = Student("Umaira", 101, 35)

student1.display()
student1.result()