import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,6,18])
y=np.array([3,10,12,20])
plt.plot(x,y,color='green',marker='o',mfc='blue',mec='black',linestyle='dotted')
plt.title('Line Diagram')
plt.xlabel('X-Axis')
plt.ylabel('y-Axis')
plt.show()
