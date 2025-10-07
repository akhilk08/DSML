import numpy as np
a1=np.array([1,2,3])
a2=np.array([1,2,3])
print("First array:",a1)
print("Second array:",a2)
if np.array_equal(a1,a2):
	print("Arrays are equal..!")
else:
	print("Arrays are not equal..!")
	
