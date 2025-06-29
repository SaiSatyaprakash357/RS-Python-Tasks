# 13. Create a 5×5 NumPy array of random integers (1 to 100).
#     Replace all even numbers in the array with 0.

import numpy as np

arr = np.random.randint(1, 101, size=(5, 5))

print("Original Array:")
print(arr)

arr[arr % 2 == 0] = 0

print("\nModified Array:")
print(arr)
