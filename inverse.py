import numpy as np
row=int(input("enter the rows:"))
col=int(input("enter the columns:"))
matrix=[]
print("enter the elements:")
for i in range (row):
	row=[]
for j in range (col):
	row.append (input())
matrix.append(row)
print("Matrix",matrix)
mat=np.array(matrix)
inverse=np.linalg.inv(mat)
print("inverse of the matrix")
print(inverse)
