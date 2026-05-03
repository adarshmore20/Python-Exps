# Experiment 4: Python Tuples

# -----------------------------
# 1. Creating Tuples
# -----------------------------
print("Creating Tuples")

empty_tuple = ()
print("Empty Tuple:", empty_tuple)

numbers = (10, 20, 30, 40)
print("Numbers Tuple:", numbers)

mixed = (10, "Hello", 3.14, True)
print("Mixed Tuple:", mixed)

nested = (1, 2, (3, 4, 5))
print("Nested Tuple:", nested)

implicit_tuple = 1, 2, 3, 4
print("Implicit Tuple:", implicit_tuple)

single = (10,)
print("Single Element Tuple:", single)


# -----------------------------
# 2. Tuple Concatenation
# -----------------------------
print("\nConcatenation")

t1 = (1, 2, 3)
t2 = (4, 5, 6)

combined = t1 + t2
print(combined)


# -----------------------------
# 3. Tuple Repetition
# -----------------------------
print("\nRepetition")

repeated = t1 * 2
print(repeated)


# -----------------------------
# 4. Membership Testing
# -----------------------------
print("\nMembership Testing")

print(2 in t1)
print(10 not in t1)


# -----------------------------
# 5. Length
# -----------------------------
print("\nLength")

print(len(t1))


# -----------------------------
# 6. Indexing
# -----------------------------
print("\nIndexing")

colors = ("red", "green", "blue", "yellow", "purple")

print(colors[0])
print(colors[2])
print(colors[-1])


# -----------------------------
# 7. Slicing
# -----------------------------
print("\nSlicing")

print(colors[0:3])
print(colors[2:])
print(colors[:4])
print(colors[-3:])


# -----------------------------
# 8. Built-in Functions
# -----------------------------
print("\nBuilt-in Functions")

nums = (15, 8, 22, 5, 13, 30)

print("Length:", len(nums))
print("Maximum:", max(nums))
print("Minimum:", min(nums))
print("Sum:", sum(nums))
print("Sorted:", sorted(nums))


# -----------------------------
# 9. Tuple to List Conversion
# -----------------------------
print("\nTuple to List")

tuple_data = (1, 2, 3, 4)

list_data = list(tuple_data)
print(list_data)

list_data.append(5)
print("Modified List:", list_data)

tuple_data = tuple(list_data)
print("Back to Tuple:", tuple_data)


# -----------------------------
# 10. Tuple Unpacking
# -----------------------------
print("\nTuple Unpacking")

a, b = 10, 20

print("Before Swap:", a, b)

a, b = b, a

print("After Swap:", a, b)


# -----------------------------
# 11. Manual Max and Min
# -----------------------------
print("\nManual Max and Min")

numbers = (15, 3, 8, 22, 5, 13)

max_val = numbers[0]
min_val = numbers[0]

for n in numbers:
    if n > max_val:
        max_val = n
    if n < min_val:
        min_val = n

print("Maximum:", max_val)
print("Minimum:", min_val)


# -----------------------------
# 12. Nested Tuple Traversal
# -----------------------------
print("\nNested Tuple Traversal")

data = (
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 28)
)

for name, age in data:
    print("Name:", name, "| Age:", age)


# -----------------------------
# 13. List of Tuples to Dictionary
# -----------------------------
print("\nTuple to Dictionary")

pairs = [("a", 10), ("b", 20), ("c", 30)]

dictionary = dict(pairs)

print(dictionary)


# -----------------------------
# 14. Frequency Count
# -----------------------------
print("\nFrequency Count")

t = (1, 2, 3, 2, 4, 1, 2)

frequency = {}

for item in t:
    frequency[item] = frequency.get(item, 0) + 1

print(frequency)


# -----------------------------
# 15. Tuple Comprehension
# -----------------------------
print("\nTuple Comprehension")

squares = tuple(x ** 2 for x in range(1, 6))

print(squares)


# -----------------------------
# 16. Mutable Object Inside Tuple
# -----------------------------
print("\nMutable List Inside Tuple")

t1 = (1, 2, 3, [10, 20])

t1[3][0] = 100

print(t1)


# -----------------------------
# 17. Extended Unpacking
# -----------------------------
print("\nExtended Unpacking")

t = (1, 2, 3, 4, 5, 6, 7)

a, b, *c = t

print("a =", a)
print("b =", b)
print("c =", c)
