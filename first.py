import numpy as np
# 1)
# a. Create an array of zeros with shape (4, 3)
array_zeros = np.zeros((4, 3))
print("Array of zeros:")
print(array_zeros)

# b. Create an array of ones with shape (4, 3)
array_ones = np.ones((4, 3))
print("\nArray of ones:")
print(array_ones)

# c. Create an array of numbers from 0 to 11 and reshape it to (4, 3)
array_numbers = np.arange(12).reshape(4, 3)
print("\nArray of numbers from 0 to 11:")
print(array_numbers)

# 2)


def F(x):
    return 2 * x**2 + 5


x_values = np.arange(1, 101, 1)
F_values = F(x_values)
table = np.column_stack((x_values, F_values))

print(" x   |   F(x)")
print("-------------")
for row in table:
    print(f"{row[0]: 3d}  |  {row[1]: 5d}")

# 3)


def F(x):
    return np.exp(-x)


x_values = np.arange(-10, 11, 1)
F_values = F(x_values)
table = np.column_stack((x_values, F_values))

print("  x    |    F(x)")
print("----------------")
for row in table:
    print(f"{row[0]: 3f}    |  {row[1]: .6f}")
