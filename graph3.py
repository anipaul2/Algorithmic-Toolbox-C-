#For 1<=n<=100
import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(1,100)
plt.plot(n, 7*n*n+6*n+5, label = "7n^2+6n+5")
plt.plot(n, 7*n*n, label = "7n^2")
plt.legend(loc = 'upper left')
plt.show()
