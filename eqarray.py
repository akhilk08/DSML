import numpy as np
a1=np.array([2,4,6,8])
a2=np.array([2,4,6,8])
print(a1)
print(a2)
if np.array_equal(a1,a2):
 	print("array are equal")
else:
	print("array are not equal")
