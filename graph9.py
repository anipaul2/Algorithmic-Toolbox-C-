#(logn)^3 and root n
import matplotlib.pyplot as plt
import numpy as np
n = np.linspace(1,10**15)
plt.plot(n, n**.5, label = "n^.5")
plt.plot(n, np.log(n)**3, label = "(logn)^3")
plt.legend(loc = 'upper left')
plt.show()