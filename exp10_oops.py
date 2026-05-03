# Experiment 10: Object Oriented Programming in Python

# ----------------------------------------
# 1. Class Variable
# ----------------------------------------
print("1. Class Variable")

class Demo:
    x = 100

a = Demo()
b = Demo()

print(a.x)
print(b.x)


# ----------------------------------------
# 2. Parameterized Constructor
# ----------------------------------------
print("\n2. Parameterized Constructor")

class Student:
    def __init__(self, name, ids, college):
        self.name = name
        self.ids = ids
        self.college = college

    def display_details(self):
        print("Student Name:", self.name)
        print("Student ID:", self.ids)
        print("Student College:", self.college)

student1 = Student("JOHN", 2023, "MIT")
student2 = Student("Rahul", 2024, "MIT")

student1.display_details()
student2.display_details()


# ----------------------------------------
# 3. Default Constructor
# ----------------------------------------
print("\n3. Default Constructor")

class Employee:
    def __init__(self, name="Not Assigned", salary=0):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)

e1 = Employee()
e2 = Employee("Amit", 40000)

e1.display()
e2.display()


# ----------------------------------------
# 4. Bank Account Example
# ----------------------------------------
print("\n4. Bank Account")

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)

acc = BankAccount("Sneha", 10000)

acc.deposit(2000)
acc.withdraw(1500)

acc.display()


# ----------------------------------------
# 5. Single Inheritance
# ----------------------------------------
print("\n5. Single Inheritance")

class Parent:
    def func1(self):
        print("This function is in parent class.")

class Child(Parent):
    def func2(self):
        print("This function is in child class.")

obj = Child()

obj.func1()
obj.func2()


# ----------------------------------------
# 6. Multiple Inheritance
# ----------------------------------------
print("\n6. Multiple Inheritance")

class Mother:
    mothername = ""

class Father:
    fathername = ""

class Son(Mother, Father):
    def parents(self):
        print("Father:", self.fathername)
        print("Mother:", self.mothername)

s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"

s1.parents()


# ----------------------------------------
# 7. Method Overriding
# ----------------------------------------
print("\n7. Method Overriding")

class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    def m(self):
        print("In Class2")

obj = Class2()
obj.m()


# ----------------------------------------
# 8. Using Parent Method
# ----------------------------------------
print("\n8. Parent Method Call")

class Base:
    def show(self):
        print("Base Class")

class Derived(Base):
    def show(self):
        print("Derived Class")
        Base.show(self)

d = Derived()
d.show()


# ----------------------------------------
# 9. super() Function
# ----------------------------------------
print("\n9. super()")

class A:
    def display(self):
        print("Class A")

class B(A):
    def display(self):
        print("Class B")
        super().display()

b = B()
b.display()


# ----------------------------------------
# 10. Multilevel Inheritance
# ----------------------------------------
print("\n10. Multilevel Inheritance")

class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Grandfather.__init__(self, grandfathername)

class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self, fathername, grandfathername)

    def print_name(self):
        print("Grandfather:", self.grandfathername)
        print("Father:", self.fathername)
        print("Son:", self.sonname)

s = Son("ABC", "Mukesh", "Dhirubhai")
s.print_name()


# ----------------------------------------
# 11. Hierarchical Inheritance
# ----------------------------------------
print("\n11. Hierarchical Inheritance")

class Parent:
    def func1(self):
        print("Parent Class")

class Child1(Parent):
    def func2(self):
        print("Child1 Class")

class Child2(Parent):
    def func3(self):
        print("Child2 Class")

c1 = Child1()
c2 = Child2()

c1.func1()
c1.func2()
c2.func1()
c2.func3()


# ----------------------------------------
# 12. Hybrid Inheritance
# ----------------------------------------
print("\n12. Hybrid Inheritance")

class School:
    def func1(self):
        print("School")

class Student1(School):
    def func2(self):
        print("Student1")

class Student3(Student1):
    def func4(self):
        print("Student3")

obj = Student3()

obj.func1()
obj.func2()
obj.func4()


# ----------------------------------------
# 13. Polymorphism
# ----------------------------------------
print("\n13. Polymorphism")

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

class Square(Shape):
    def area(self):
        return 4 * 4

shapes = [Circle(), Square()]

for shape in shapes:
    print(shape.area())


# ----------------------------------------
# 14. Encapsulation
# ----------------------------------------
print("\n14. Encapsulation")

class Account:
    def __init__(self):
        self.__balance = 1000

    def show_balance(self):
        print(self.__balance)

acc = Account()
acc.show_balance()


# ----------------------------------------
# 15. Abstraction
# ----------------------------------------
print("\n15. Abstraction")

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car Starts")

c = Car()
c.start()
