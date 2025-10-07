import numpy as np
n=int(input("enter the size of array:"))
print("enter the elements:")
elements=list(map(float,input().split()))
matrix=np.array(elements).reshape(n,n)
print("matrix")
print(matrix)
trace=np.trace(matrix)
print(trace)
