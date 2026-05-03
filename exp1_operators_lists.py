# Experiment 1: Python Operators and Lists

# -----------------------------
# Arithmetic Operators
# -----------------------------
x = 10
y = 20

print("Arithmetic Operators")
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)
print("x % y =", x % y)
print("x // y =", x // y)
print("x ** y =", x ** y)

# -----------------------------
# Comparison Operators
# -----------------------------
x = 20
y = 25

print("\nComparison Operators")
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

# -----------------------------
# Logical Operators
# -----------------------------
x = 10
y = 20

print("\nLogical Operators")
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# -----------------------------
# Bitwise Operators
# -----------------------------
a = 10
b = 4

print("\nBitwise Operators")
print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("~a =", ~a)
print("a << 2 =", a << 2)
print("a >> 2 =", a >> 2)

# -----------------------------
# Membership Operators
# -----------------------------
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("\nMembership Operators")
print("10 in list:", 10 in lst)
print("7 in list:", 7 in lst)
print("23 not in list:", 23 not in lst)

# -----------------------------
# Identity Operators
# -----------------------------
x = 6
print("\nIdentity Operators")
print(type(x) is int)

x = 4.5
print(type(x) is not int)

# -----------------------------
# Reverse Loop
# -----------------------------
print("\nReverse Loop")
for i in range(5, 1, -1):
    print(i)

# -----------------------------
# List Creation
# -----------------------------
a = [1, 2, 3, 4, 5]
b = ['apple', 'banana', 'cherry']
c = [1, 'hello', 3.14, True]

print("\nLists")
print(a)
print(b)
print(c)

# -----------------------------
# Accessing List Elements
# -----------------------------
a = [10, 20, "Python", 40, True]

print("\nAccessing Elements")
print(a[0])
print(a[1])
print(a[2])

# -----------------------------
# List using list()
# -----------------------------
a = list((1, 2, 3, 'apple', 4.5))
print("\nList using list()")
print(a)

# -----------------------------
# Repeated Elements
# -----------------------------
a = [2] * 5
print("\nRepeated Elements")
print(a)

# -----------------------------
# List Slicing
# -----------------------------
a = [10, 20, 30, 40, 50]

print("\nList Slicing")
print(a[0])
print(a[4])
print(a[-1])
print(a[1:4])

# -----------------------------
# Adding Elements
# -----------------------------
a = []

a.append(10)
a.insert(0, 5)
a.extend([15, 20, 25])

print("\nAdding Elements")
print(a)

# -----------------------------
# Removing Elements
# -----------------------------
a.remove(15)
print("\nAfter remove:", a)

popped = a.pop(1)
print("Popped:", popped)
print(a)

del a[0]
print("After del:", a)

# -----------------------------
# Iterating List
# -----------------------------
print("\nIterating List")
fruits = ['apple', 'banana', 'cherry']

for item in fruits:
    print(item)

# -----------------------------
# Nested List
# -----------------------------
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\nNested List")
print(matrix[1])
print(matrix[1][2])

# -----------------------------
# List Comprehension
# -----------------------------
squares = [x**2 for x in range(1, 6)]

print("\nList Comprehension")
print(squares)

# -----------------------------
# More Slicing
# -----------------------------
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("\nAdvanced Slicing")
print(a[1:4])
print(a[:])
print(a[2:])
print(a[:3])
print(a[::2])
print(a[::-1])

# -----------------------------
# Tuple Mutability Example
# -----------------------------
t1 = (1, 2, 3, 4, [11, 22])
t1[4][0] = 100

print("\nTuple with Mutable List")
print(t1)

# -----------------------------
# Tuple Unpacking
# -----------------------------
t1 = (1, 2, 3, 4, 5, 6, 7)

a, b, *c = t1

print("\nTuple Unpacking")
print("a =", a)
print("b =", b)
print("c =", c)
