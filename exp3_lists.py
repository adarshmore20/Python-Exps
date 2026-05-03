# Experiment 3: Python Lists

# -----------------------------
# 1. Creating Lists
# -----------------------------
print("Creating Lists")

a = [1, 2, 3, 4, 5]
b = ['apple', 'banana', 'cherry']
c = [1, 'hello', 3.14, True]

print(a)
print(b)
print(c)


# -----------------------------
# 2. Accessing List Elements
# -----------------------------
print("\nAccessing Elements")

a = [10, 20, "Python", 40, True]

print(a[0])
print(a[1])
print(a[2])


# -----------------------------
# 3. Creating List using list()
# -----------------------------
print("\nUsing list()")

a = list((1, 2, 3, 'apple', 4.5))
print(a)


# -----------------------------
# 4. Repeated Elements
# -----------------------------
print("\nRepeated Elements")

a = [2] * 5
b = [0] * 7

print(a)
print(b)


# -----------------------------
# 5. Slicing
# -----------------------------
print("\nSlicing")

a = [10, 20, 30, 40, 50]

print(a[0])
print(a[4])
print(a[-1])
print(a[1:4])


# -----------------------------
# 6. Adding Elements
# -----------------------------
print("\nAdding Elements")

a = []

a.append(10)
print("After append:", a)

a.insert(0, 5)
print("After insert:", a)

a.extend([15, 20, 25])
print("After extend:", a)


# -----------------------------
# 7. Appending using Loop
# -----------------------------
print("\nAppending with Loop")

nums = []

for i in range(5):
    nums.append(i)

print(nums)


# -----------------------------
# 8. Insert Tuple into List
# -----------------------------
print("\nInsert Tuple")

list1 = [1, 2, 3, 4, 5]
num_tuple = (6, 7, 8)

list1.insert(2, num_tuple)

print(list1)


# -----------------------------
# 9. Insert Dictionary
# -----------------------------
print("\nInsert Dictionary")

my_list = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25}
]

new_dict = {'name': 'Charlie', 'age': 40}

my_list.append(new_dict)

print(my_list)


# -----------------------------
# 10. Merge Lists
# -----------------------------
print("\nMerge Lists")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1 = list1 + list2

print(list1)


# -----------------------------
# 11. Remove Elements
# -----------------------------
print("\nRemove Elements")

a = [10, 20, 30, 40, 50]

a.remove(30)
print("After remove:", a)

popped = a.pop(1)
print("Popped:", popped)
print(a)

del a[0]
print("After del:", a)


# -----------------------------
# 12. Update Elements
# -----------------------------
print("\nUpdate Elements")

a = [10, 20, 30, 40, 50]
a[1] = 25

print(a)


# -----------------------------
# 13. Iterating
# -----------------------------
print("\nIterating")

fruits = ['apple', 'banana', 'cherry']

for item in fruits:
    print(item)


# -----------------------------
# 14. Nested List
# -----------------------------
print("\nNested List")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1])
print(matrix[1][2])


# -----------------------------
# 15. List Comprehension
# -----------------------------
print("\nList Comprehension")

squares = [x**2 for x in range(1, 6)]

print(squares)


# -----------------------------
# 16. Advanced Slicing
# -----------------------------
print("\nAdvanced Slicing")

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[1:4])
print(a[:])
print(a[2:])
print(a[:3])
print(a[::2])
print(a[::-1])


# -----------------------------
# 17. Membership Testing
# -----------------------------
print("\nMembership Testing")

print(5 in a)
print(20 not in a)


# -----------------------------
# 18. Length of List
# -----------------------------
print("\nLength")

print(len(a))
