# 14. Create two 3×3 NumPy arrays with random integers.
#     Write code to check and return a boolean array showing element-wise equality.

import numpy as np

array1 = np.random.randint(0, 10, (3, 3))
array2 = np.random.randint(0, 10, (3, 3))

print("Array 1:")
print(array1)
print("\nArray 2:")
print(array2)

equal_elements= (array1 == array2)

print("\nElement-wise equality:")
print(equal_elements)
