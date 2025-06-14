import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# NumPy Operations

print("=== NumPy Operations ===")

# 1. Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.arange(6, 16)
arr3 = np.linspace(0, 1, 5)
arr4 = np.random.randint(10, 100, (3, 3))

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Linearly spaced array:", arr3)
print("Random 3x3 Array:\n", arr4)

# 2. Basic operations
print("Array1 + 10:", arr1 + 10)
print("Array2 * 2:", arr2 * 2)
print("Element-wise addition:", arr1 + arr2[:5])

# 3. Slicing and reshaping
print("Sliced Array2 [2:7]:", arr2[2:7])
reshaped = arr2[:6].reshape(2, 3)
print("Reshaped Array2 to 2x3:\n", reshaped)

# 4. Aggregations
print("Sum of Array4:", np.sum(arr4))
print("Max of Array4:", np.max(arr4))
print("Mean of Array4:", np.mean(arr4))
print("Transpose of Array4:\n", np.transpose(arr4))

# Pandas Operations

print("\n=== Pandas Operations ===")

# 1. Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 28],
    'Score': [85, 90, 88, 76, 92],
    'Department': ['CS', 'Math', 'CS', 'Math', 'Physics']
}
df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

# 2. Basic info and stats
print("\nDataFrame Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# 3. Indexing and filtering
print("\nNames with Score > 85:")
print(df[df['Score'] > 85])

# 4. Groupby
print("\nAverage Score by Department:")
print(df.groupby('Department')['Score'].mean())

# 5. Adding a new column
df['Passed'] = df['Score'] >= 80
print("\nDataFrame with 'Passed' Column:")
print(df)

# Matplotlib Visualizations

print("\n=== Matplotlib Plots ===")

# 1. Line Plot
plt.figure()
plt.plot(df['Name'], df['Score'], marker='o', linestyle='-', color='blue')
plt.title('Scores of Students')
plt.xlabel('Name')
plt.ylabel('Score')
plt.grid(True)

# 2. Bar Plot
plt.figure()
plt.bar(df['Name'], df['Age'], color='orange')
plt.title('Age of Students')
plt.xlabel('Name')
plt.ylabel('Age')

# 3. Scatter Plot
plt.figure()
plt.scatter(df['Age'], df['Score'], color='green')
plt.title('Age vs Score')
plt.xlabel('Age')
plt.ylabel('Score')

# 4. Pie Chart
plt.figure()
plt.pie(df['Score'], labels=df['Name'], autopct='%1.1f%%', startangle=90)
plt.title('Score Distribution')

# 5. Histogram
plt.figure()
plt.hist(df['Age'], bins=5, color='purple', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')

# 6. Box Plot
plt.figure()
plt.boxplot(df['Score'])
plt.title('Boxplot of Scores')

plt.show()
