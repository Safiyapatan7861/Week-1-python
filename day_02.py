for i in range(5):
    print("Hello")
for i in range (1,8):
    print(i)
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()    
i = 1
while i <= 5:
    print(i)
    i = i + 1
for i in range(1, 6):
    if i == 3:
        break
    print(i)
def hello():
    print("Hello World")
hello()
print(len("python"))
print(max(10,7,8,34))
print(sum([10,27,77,82]))
def add():
    a = 10
    b = 20
    print(a + b)
add()
def greet(name):
    print("Hello", name)
greet("Rahul")
greet("Priya")
students = ["Rahul", "Priya", "Arun", "Sneha"]
print(students)
numbers = [10, 20, 30, 40, 50]
print(numbers)
fruits = ["Apple", "Banana"]
fruits.append("Mango")
print(fruits)
fruits = ["Apple", "Banana"]
fruits.insert(1, "Mango")
print(fruits)
fruits = ["Apple", "Banana", "Mango"]
fruits.remove("Banana")
print(fruits)
fruits = ["Apple", "Banana", "Mango"]
fruits.pop()
print(fruits)
numbers = (10, 20, 10, 30, 10)
print(numbers.count(10))
numbers = {101, 102, 103, 101, 104}
print(numbers)