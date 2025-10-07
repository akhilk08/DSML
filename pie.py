import numpy as np
import matplotlib.pyplot as plt
x=['java','python','php','javascript','c#']
y=np.array([22.2,17.6,8.8,8,7.7])
plt.pie(y,labels=x)
plt.show()
