# Experiment 9: NumPy, Pandas, Matplotlib and SciPy

# ----------------------------------------
# Import Libraries
# ----------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# ----------------------------------------
# 1. NumPy Array Creation
# ----------------------------------------
print("1. NumPy Array Creation")

arr = np.array([10, 20, 30, 40, 50])

print(arr)


# ----------------------------------------
# 2. Array Operations
# ----------------------------------------
print("\n2. Array Operations")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Multiplication:", a * b)


# ----------------------------------------
# 3. Matrix Operations
# ----------------------------------------
print("\n3. Matrix Operations")

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

print("Matrix Addition:\n", matrix1 + matrix2)
print("Matrix Multiplication:\n", np.dot(matrix1, matrix2))


# ----------------------------------------
# 4. Statistical Functions
# ----------------------------------------
print("\n4. NumPy Statistics")

data = np.array([10, 20, 30, 40, 50])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))


# ----------------------------------------
# 5. Array Reshaping
# ----------------------------------------
print("\n5. Reshaping")

arr = np.arange(12)

print(arr.reshape(3, 4))


# ----------------------------------------
# 6. Pandas Series
# ----------------------------------------
print("\n6. Pandas Series")

series = pd.Series([10, 20, 30, 40])

print(series)


# ----------------------------------------
# 7. Pandas DataFrame
# ----------------------------------------
print("\n7. DataFrame")

data = {
    "Name": ["Aman", "Rahul", "Priya"],
    "Marks": [85, 92, 88]
}

df = pd.DataFrame(data)

print(df)


# ----------------------------------------
# 8. DataFrame Information
# ----------------------------------------
print("\n8. DataFrame Info")

print(df.head())
print(df.describe())


# ----------------------------------------
# 9. Selecting Columns
# ----------------------------------------
print("\n9. Column Selection")

print(df["Name"])


# ----------------------------------------
# 10. Adding New Column
# ----------------------------------------
print("\n10. Adding Column")

df["Grade"] = ["B", "A", "A"]

print(df)


# ----------------------------------------
# 11. Filtering Data
# ----------------------------------------
print("\n11. Filtering")

print(df[df["Marks"] > 85])


# ----------------------------------------
# 12. Matplotlib Line Plot
# ----------------------------------------
print("\n12. Line Plot")

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


# ----------------------------------------
# 13. Bar Graph
# ----------------------------------------
print("\n13. Bar Graph")

students = ["Aman", "Rahul", "Priya"]
marks = [85, 92, 88]

plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()


# ----------------------------------------
# 14. Pie Chart
# ----------------------------------------
print("\n14. Pie Chart")

sizes = [40, 35, 25]
labels = ["Python", "Java", "C++"]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Programming Language Usage")
plt.show()


# ----------------------------------------
# 15. Histogram
# ----------------------------------------
print("\n15. Histogram")

data = np.random.randn(100)

plt.hist(data)
plt.title("Histogram")
plt.show()


# ----------------------------------------
# 16. Scatter Plot
# ----------------------------------------
print("\n16. Scatter Plot")

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()


# ----------------------------------------
# 17. SciPy Mean
# ----------------------------------------
print("\n17. SciPy Statistics")

values = [10, 20, 30, 40, 50]

print("Mean:", stats.tmean(values))


# ----------------------------------------
# 18. Mode
# ----------------------------------------
print("\n18. Mode")

print(stats.mode(values))


# ----------------------------------------
# 19. Normal Distribution
# ----------------------------------------
print("\n19. Normal Distribution")

sample = stats.norm.rvs(size=10)

print(sample)


# ----------------------------------------
# 20. Correlation
# ----------------------------------------
print("\n20. Correlation")

x = [10, 20, 30, 40, 50]
y = [15, 25, 35, 45, 55]

corr = np.corrcoef(x, y)

print(corr)
