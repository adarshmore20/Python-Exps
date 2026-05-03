# Experiment 8: Python Packages

# ----------------------------------------
# 1. Importing Built-in Packages
# ----------------------------------------
print("1. Built-in Packages")

import math
import random
import datetime

print("Square Root:", math.sqrt(64))
print("Random Number:", random.randint(1, 100))
print("Current Date:", datetime.date.today())


# ----------------------------------------
# 2. Using math Package
# ----------------------------------------
print("\n2. Math Package")

print("Pi:", math.pi)
print("Power:", math.pow(2, 5))
print("Factorial:", math.factorial(5))


# ----------------------------------------
# 3. Using random Package
# ----------------------------------------
print("\n3. Random Package")

print("Random Float:", random.random())
print("Random Choice:", random.choice(["Python", "Java", "C++"]))


# ----------------------------------------
# 4. Using datetime Package
# ----------------------------------------
print("\n4. Datetime Package")

now = datetime.datetime.now()

print("Current Time:", now)
print("Year:", now.year)
print("Month:", now.month)


# ----------------------------------------
# 5. Import Specific Function
# ----------------------------------------
print("\n5. Import Specific Function")

from math import sqrt

print("sqrt(49):", sqrt(49))


# ----------------------------------------
# 6. Alias Import
# ----------------------------------------
print("\n6. Alias Import")

import math as m

print("Cube Root Approximation:", m.pow(27, 1/3))


# ----------------------------------------
# 7. Creating a Simulated Package Function
# ----------------------------------------
print("\n7. Simulated Package")

def addition(a, b):
    return a + b

print("Addition:", addition(10, 20))


# ----------------------------------------
# 8. String Package Example
# ----------------------------------------
print("\n8. String Package")

import string

print("Lowercase Letters:", string.ascii_lowercase)
print("Digits:", string.digits)


# ----------------------------------------
# 9. Statistics Package
# ----------------------------------------
print("\n9. Statistics Package")

import statistics

data = [10, 20, 30, 40, 50]

print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))


# ----------------------------------------
# 10. OS Package
# ----------------------------------------
print("\n10. OS Package")

import os

print("Current Directory:", os.getcwd())


# ----------------------------------------
# 11. sys Package
# ----------------------------------------
print("\n11. Sys Package")

import sys

print("Python Version:", sys.version)


# ----------------------------------------
# 12. Calendar Package
# ----------------------------------------
print("\n12. Calendar Package")

import calendar

print(calendar.month(2026, 5))


# ----------------------------------------
# 13. Decimal Package
# ----------------------------------------
print("\n13. Decimal Package")

from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.2")

print("Exact Decimal Addition:", a + b)


# ----------------------------------------
# 14. Collections Package
# ----------------------------------------
print("\n14. Collections Package")

from collections import Counter

text = "pythonpackage"

count = Counter(text)

print(count)


# ----------------------------------------
# 15. Time Package
# ----------------------------------------
print("\n15. Time Package")

import time

print("Current Timestamp:", time.time())


# ----------------------------------------
# 16. JSON Package
# ----------------------------------------
print("\n16. JSON Package")

import json

student = {
    "name": "ADM",
    "age": 20
}

json_data = json.dumps(student)

print(json_data)


# ----------------------------------------
# 17. Package Example with Function
# ----------------------------------------
print("\n17. Custom Utility")

def multiply(a, b):
    return a * b

print(multiply(5, 6))


# ----------------------------------------
# 18. Using dir()
# ----------------------------------------
print("\n18. dir()")

print(dir(math)[:10])


# ----------------------------------------
# 19. Help on Package
# ----------------------------------------
print("\n19. Package Name")

print(math.__name__)


# ----------------------------------------
# 20. Practical Example
# ----------------------------------------
print("\n20. Random Password Generator")

chars = string.ascii_letters + string.digits

password = ''.join(random.choice(chars) for _ in range(8))

print("Generated Password:", password)
