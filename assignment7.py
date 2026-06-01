#difference between python list and numpy array
import numpy as np

# Python List Example
list1 = [1, 2, 3]
list2 = [4, 5, 6]

print("Python Lists:")
#Python List is a built-in Python data structure
print("List 1:", list1)
print("List 2:", list2)
print("Using + operator:")
print(list1 + list2)  # Concatenation

print("\n" + "-"*40 + "\n")

# NumPy Array Example
array1 = np.array([1, 2, 3]) #NumPy Array is provided by the NumPy library.")
array2 = np.array([4, 5, 6])

print("NumPy Arrays:")
print("Array 1:", array1)
print("Array 2:", array2)

print("Using + operator:")
print(array1 + array2)  # Element-wise addition

print("\n" + "-"*40 + "\n")

print("Key Differences between Python Lists and NumPy Arrays:")
print("\n1. Python Lists are general-purpose containers.")
print("   NumPy Arrays are optimized for numerical computations.")
print("\n2. Python Lists can store different data types.")
print("   NumPy Arrays usually store elements of the same data type.")
print("\n3. Python Lists are slower for numerical operations.")
print("   NumPy Arrays are faster for numerical operations.")
print("\n4. Python Lists use more memory.")
print("   NumPy Arrays use less memory.")
print("\n5. Python Lists do not support direct element-wise arithmetic.")
print("   NumPy Arrays support direct element-wise arithmetic.")