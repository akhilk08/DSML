import numpy as np
a=np.array([[2,4,6,8],[3,6,9,12]])
sum_all=np.sum(a)
print(a)
sum_col=np.sum(a,axis=0)
sum_row=np.sum(a,axis=1)
print("sum of all elements:",sum_all)
print("sum of column:",sum_col)
print("sum of row:",sum_row)

