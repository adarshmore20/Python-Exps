# Experiment 6: Python Dictionary

# ----------------------------------------
# 1. Creating Dictionaries
# ----------------------------------------
print("1. Creating Dictionaries")

student = {
    "name": "ADM",
    "age": 20,
    "course": "Python"
}

print(student)


# ----------------------------------------
# 2. Empty Dictionary
# ----------------------------------------
print("\n2. Empty Dictionary")

empty_dict = {}

print(empty_dict)


# ----------------------------------------
# 3. Using dict() Constructor
# ----------------------------------------
print("\n3. dict() Constructor")

person = dict(name="Rahul", age=21, city="Pune")

print(person)


# ----------------------------------------
# 4. Accessing Values
# ----------------------------------------
print("\n4. Accessing Values")

print(student["name"])
print(student.get("age"))


# ----------------------------------------
# 5. Adding Elements
# ----------------------------------------
print("\n5. Adding Elements")

student["marks"] = 95

print(student)


# ----------------------------------------
# 6. Updating Values
# ----------------------------------------
print("\n6. Updating Values")

student["age"] = 22

print(student)


# ----------------------------------------
# 7. Removing Elements
# ----------------------------------------
print("\n7. Removing Elements")

student.pop("course")

print(student)


# ----------------------------------------
# 8. popitem()
# ----------------------------------------
print("\n8. popitem()")

data = {
    "a": 1,
    "b": 2,
    "c": 3
}

removed = data.popitem()

print("Removed:", removed)
print(data)


# ----------------------------------------
# 9. del Keyword
# ----------------------------------------
print("\n9. del Keyword")

info = {
    "x": 10,
    "y": 20
}

del info["x"]

print(info)


# ----------------------------------------
# 10. Dictionary Length
# ----------------------------------------
print("\n10. Length")

print(len(student))


# ----------------------------------------
# 11. Iterating Through Dictionary
# ----------------------------------------
print("\n11. Iteration")

for key, value in student.items():
    print(key, ":", value)


# ----------------------------------------
# 12. Keys, Values, Items
# ----------------------------------------
print("\n12. keys(), values(), items()")

print(student.keys())
print(student.values())
print(student.items())


# ----------------------------------------
# 13. Membership Testing
# ----------------------------------------
print("\n13. Membership Testing")

print("name" in student)
print("salary" not in student)


# ----------------------------------------
# 14. Nested Dictionary
# ----------------------------------------
print("\n14. Nested Dictionary")

students = {
    "student1": {"name": "Aman", "marks": 90},
    "student2": {"name": "Priya", "marks": 85}
}

print(students)
print(students["student1"]["name"])


# ----------------------------------------
# 15. Dictionary Comprehension
# ----------------------------------------
print("\n15. Dictionary Comprehension")

squares = {x: x*x for x in range(1, 6)}

print(squares)


# ----------------------------------------
# 16. Copy Dictionary
# ----------------------------------------
print("\n16. Copy Dictionary")

copy_student = student.copy()

print(copy_student)


# ----------------------------------------
# 17. clear()
# ----------------------------------------
print("\n17. clear()")

temp = {"a": 1, "b": 2}

temp.clear()

print(temp)


# ----------------------------------------
# 18. setdefault()
# ----------------------------------------
print("\n18. setdefault()")

student.setdefault("city", "Mumbai")

print(student)


# ----------------------------------------
# 19. update()
# ----------------------------------------
print("\n19. update()")

student.update({"marks": 98, "grade": "A"})

print(student)


# ----------------------------------------
# 20. Frequency Count
# ----------------------------------------
print("\n20. Frequency Count")

text = "dictionary"

freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

print(freq)


# ----------------------------------------
# 21. Merge Dictionaries
# ----------------------------------------
print("\n21. Merge Dictionaries")

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

merged = {**d1, **d2}

print(merged)


# ----------------------------------------
# 22. Sorting Dictionary
# ----------------------------------------
print("\n22. Sorting Dictionary")

marks = {
    "A": 85,
    "B": 92,
    "C": 78
}

sorted_marks = dict(sorted(marks.items()))

print(sorted_marks)
