import numpy as np
import matplotlib.pyplot as plt
x1=np.array([2,4,6,8])
y1=np.array([3,6,9,12])
x2=np.array([4,8,12,16])
y2=np.array([5,10,15,20])
plt.plot(x1,y1,color='red',marker='o',mfc='blue',mec='yellow')
plt.plot(x2,y2,color='blue',marker='o',mfc='red',mec='black')
plt.title('Legend Diagram')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend(['red','blue'])
plt.show()
