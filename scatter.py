import numpy as np
import matplotlib.pyplot as plt
maths=np.array([88,92,180,89,100,80,60,100,80,34])
science=np.array([35,79,79,48,100,88,32,45,20,30])
plt.scatter(maths,science,color='red',marker='o')
plt.grid(True)
plt.title('Scatter Plot')
plt.xlabel('maths')
plt.ylabel('science')
plt.show()
