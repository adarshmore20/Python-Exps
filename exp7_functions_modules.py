# Experiment 7: Functions and Modules

import math
import random

# ----------------------------------------
# 1. Simple Function
# ----------------------------------------
print("1. Simple Function")

def greet():
    print("Hello, Welcome to Python Lab")

greet()


# ----------------------------------------
# 2. Function with Parameters
# ----------------------------------------
print("\n2. Function with Parameters")

def add(a, b):
    return a + b

print("Sum:", add(10, 20))


# ----------------------------------------
# 3. Function with Default Arguments
# ----------------------------------------
print("\n3. Default Arguments")

def student(name, course="Python"):
    print("Name:", name)
    print("Course:", course)

student("ADM")
student("Rahul", "Data Science")


# ----------------------------------------
# 4. Keyword Arguments
# ----------------------------------------
print("\n4. Keyword Arguments")

def details(name, age):
    print("Name:", name)
    print("Age:", age)

details(age=20, name="Aman")


# ----------------------------------------
# 5. Arbitrary Arguments (*args)
# ----------------------------------------
print("\n5. *args")

def total_sum(*numbers):
    print("Sum:", sum(numbers))

total_sum(10, 20, 30, 40)


# ----------------------------------------
# 6. Arbitrary Keyword Arguments (**kwargs)
# ----------------------------------------
print("\n6. **kwargs")

def display_info(**data):
    for key, value in data.items():
        print(key, ":", value)

display_info(name="ADM", age=20, city="Pune")


# ----------------------------------------
# 7. Recursive Function
# ----------------------------------------
print("\n7. Recursive Function")

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))


# ----------------------------------------
# 8. Lambda Function
# ----------------------------------------
print("\n8. Lambda Function")

square = lambda x: x * x

print(square(6))


# ----------------------------------------
# 9. Function Returning Multiple Values
# ----------------------------------------
print("\n9. Multiple Return Values")

def calc(a, b):
    return a + b, a - b, a * b

x, y, z = calc(10, 5)

print("Addition:", x)
print("Subtraction:", y)
print("Multiplication:", z)


# ----------------------------------------
# 10. Local and Global Variables
# ----------------------------------------
print("\n10. Local and Global Variables")

x = 100

def demo():
    x = 50
    print("Local x:", x)

demo()
print("Global x:", x)


# ----------------------------------------
# 11. math Module
# ----------------------------------------
print("\n11. math Module")

print("Square Root:", math.sqrt(25))
print("Power:", math.pow(2, 3))
print("Pi:", math.pi)


# ----------------------------------------
# 12. random Module
# ----------------------------------------
print("\n12. random Module")

print("Random Integer:", random.randint(1, 100))
print("Random Choice:", random.choice(["Python", "Java", "C++"]))


# ----------------------------------------
# 13. User-defined Module Style
# ----------------------------------------
print("\n13. Simulated Module Function")

def multiply(a, b):
    return a * b

print("Product:", multiply(5, 4))


# ----------------------------------------
# 14. map() with Function
# ----------------------------------------
print("\n14. map() Function")

nums = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x*x, nums))

print(squares)


# ----------------------------------------
# 15. filter() Function
# ----------------------------------------
print("\n15. filter() Function")

even = list(filter(lambda x: x % 2 == 0, nums))

print(even)


# ----------------------------------------
# 16. Function to Check Prime
# ----------------------------------------
print("\n16. Prime Check")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(17))


# ----------------------------------------
# 17. Fibonacci Function
# ----------------------------------------
print("\n17. Fibonacci Series")

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)
print()


# ----------------------------------------
# 18. Docstring
# ----------------------------------------
print("\n18. Docstring")

def info():
    """This function displays Python experiment information"""
    print("Functions and Modules")

print(info.__doc__)


# ----------------------------------------
# 19. Scope Example
# ----------------------------------------
print("\n19. Scope")

count = 10

def show():
    global count
    count += 5
    print(count)

show()


# ----------------------------------------
# 20. Anonymous Function in Sorting
# ----------------------------------------
print("\n20. Sorting using Lambda")

students = [
    ("Aman", 85),
    ("Rahul", 92),
    ("Priya", 88)
]

students.sort(key=lambda x: x[1])

print(students)
