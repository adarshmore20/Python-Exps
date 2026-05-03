# Experiment 5: Lambda Functions, List Comprehension and Sets

# ----------------------------------------
# 1. Basic Lambda Function
# ----------------------------------------
print("1. Basic Lambda Function")

func = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print(func(5))
print(func(-3))
print(func(0))


# ----------------------------------------
# 2. Lambda with List Comprehension
# ----------------------------------------
print("\n2. Lambda with List Comprehension")

funcs = [lambda arg=x: arg * 10 for x in range(1, 5)]

for f in funcs:
    print(f())


# ----------------------------------------
# 3. Lambda Returning Multiple Values
# ----------------------------------------
print("\n3. Lambda Returning Multiple Results")

calc = lambda x, y: (x + y, x * y)

result = calc(3, 4)

print("Sum:", result[0])
print("Product:", result[1])


# ----------------------------------------
# 4. Basic List Comprehension
# ----------------------------------------
print("\n4. List Comprehension")

squares = [x**2 for x in range(1, 6)]

print(squares)


# ----------------------------------------
# 5. List Comprehension with Condition
# ----------------------------------------
print("\n5. List Comprehension with Condition")

even_numbers = [x for x in range(1, 21) if x % 2 == 0]

print(even_numbers)


# ----------------------------------------
# 6. String Transformation using List Comprehension
# ----------------------------------------
print("\n6. String Uppercase")

words = ["python", "lab", "experiment"]

upper_words = [word.upper() for word in words]

print(upper_words)


# ----------------------------------------
# 7. Creating Sets
# ----------------------------------------
print("\n7. Creating Sets")

s1 = {1, 2, 3}
print(s1)

s2 = set([4, 5, 6])
print(s2)

s3 = set()
print(s3)


# ----------------------------------------
# 8. Duplicate Removal
# ----------------------------------------
print("\n8. Duplicate Removal")

s = {"Python", "Python", "Lab"}

print(s)


# ----------------------------------------
# 9. Add and Remove Elements
# ----------------------------------------
print("\n9. Add and Remove")

s = {"a", "b", "c"}

s.add("d")
print("After add:", s)

s.remove("c")
print("After remove:", s)


# ----------------------------------------
# 10. Union of Sets
# ----------------------------------------
print("\n10. Union")

a = {"x", "y"}
b = {"y", "z"}

print(a | b)
print(a.union(b))


# ----------------------------------------
# 11. Intersection
# ----------------------------------------
print("\n11. Intersection")

a = {1, 2, 3}
b = {2, 3, 4}

print(a & b)
print(a.intersection(b))


# ----------------------------------------
# 12. Difference
# ----------------------------------------
print("\n12. Difference")

print(a - b)
print(a.difference(b))


# ----------------------------------------
# 13. Symmetric Difference
# ----------------------------------------
print("\n13. Symmetric Difference")

print(a ^ b)


# ----------------------------------------
# 14. Clear Set
# ----------------------------------------
print("\n14. Clear")

s = {1, 2, 3}

s.clear()

print(s)


# ----------------------------------------
# 15. Subset and Superset
# ----------------------------------------
print("\n15. Subset and Superset")

A = {1, 2}
B = {1, 2, 3, 4}

print("A subset of B:", A.issubset(B))
print("B superset of A:", B.issuperset(A))


# ----------------------------------------
# 16. Membership Testing
# ----------------------------------------
print("\n16. Membership Testing")

print(3 in {1, 2, 3})
print(10 not in {1, 2, 3})


# ----------------------------------------
# 17. Iterating through Set
# ----------------------------------------
print("\n17. Iteration")

for item in {1, 2, 3}:
    print(item)


# ----------------------------------------
# 18. Set Comprehension
# ----------------------------------------
print("\n18. Set Comprehension")

squares_set = {x*x for x in range(5)}

print(squares_set)


# ----------------------------------------
# 19. Frozenset
# ----------------------------------------
print("\n19. Frozenset")

fs = frozenset([1, 2, 3, 4])

print(fs)


# ----------------------------------------
# 20. Practical Example
# ----------------------------------------
print("\n20. Remove Duplicates from List")

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = list(set(numbers))

print(unique_numbers)
