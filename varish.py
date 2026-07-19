import numpy as np

# 1. Array banana
arr = np.array([10, 20, 30, 40, 50])

print("Original Array:")
print(arr)

# 2. Array Information
print("\nShape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)

# 3. Mathematical Operations
print("\nAddition (+5):", arr + 5)
print("Multiplication (*2):", arr * 2)

# 4. Statistics
print("\nSum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# 5. 2D Array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\n2D Array:")
print(matrix)

# 6. Row aur Column
print("\nFirst Row:", matrix[0])
print("Second Column:", matrix[:, 1])

# 7. Reshape
new_arr = np.arange(1, 13).reshape(3, 4)

print("\nReshaped Array:")
print(new_arr)

# 8. Random Numbers
random_array = np.random.randint(1, 101, size=(3, 3))

print("\nRandom Array:")
print(random_array)