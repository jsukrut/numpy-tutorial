import numpy as np
import sys



np_digits = np.array([
			[1, 2, 3],
			[4, 5, 6],
			[6, 7, 9],
		])

print(np_digits)
print("bytes taken",sys.getsizeof(np_digits))
print(np_digits.max())

py_digits = [[1, 2, 3],
			 [4, 5, 6],
			[6, 7, 9],
			]
print(py_digits)
print("bytes taken",sys.getsizeof(py_digits))
print(max(py_digits))




