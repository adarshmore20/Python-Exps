# Experiment 2: Loops and Basic DSA Programs

# -----------------------------
# 1. Basic For Loop
# -----------------------------
print("1. Basic For Loop")
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)


# -----------------------------
# 2. Sum of Elements in a List
# -----------------------------
print("\n2. Sum of Elements")

arr = [10, 20, 30, 40, 50]
total = 0

for val in arr:
    total += val

print("Sum =", total)


# -----------------------------
# 3. Find Maximum Element
# -----------------------------
print("\n3. Maximum Element")

arr = [12, 45, 23, 51, 19, 8]
max_val = arr[0]

for num in arr:
    if num > max_val:
        max_val = num

print("Maximum Element:", max_val)


# -----------------------------
# 4. Loop Through Dictionary
# -----------------------------
print("\n4. Dictionary Traversal")

student = {
    "name": "Mrunal",
    "age": 21,
    "marks": 92
}

for key, value in student.items():
    print(key, ":", value)


# -----------------------------
# 5. Reverse a String
# -----------------------------
print("\n5. Reverse String")

string = "Python"
reversed_str = ""

for ch in string:
    reversed_str = ch + reversed_str

print("Reversed:", reversed_str)


# -----------------------------
# 6. Frequency Count
# -----------------------------
print("\n6. Frequency Count")

arr = [1, 2, 2, 3, 1, 4, 2]
freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

print(freq)


# -----------------------------
# 7. Even Numbers
# -----------------------------
print("\n7. Even Numbers")

for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")

print()


# -----------------------------
# 8. Multiplication Table
# -----------------------------
print("\n8. Multiplication Table")

n = 5

for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")


# -----------------------------
# 9. Factorial
# -----------------------------
print("\n9. Factorial")

num = 5
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)


# -----------------------------
# 10. Prime Check
# -----------------------------
print("\n10. Prime Check")

num = 17
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "is Prime")
else:
    print(num, "is Not Prime")
