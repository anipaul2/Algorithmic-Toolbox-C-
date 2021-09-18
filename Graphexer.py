#Here n is n^0.1 and (logn)^5
import matplotlib.pyplot as plt
import numpy as np
n = np.linspace(1,10**-0.5)
plt.plot(n, n ** .1, label = "n^.1")
plt.plot(n, np.log(n)**5, label = "(logn)^5")
plt.legend(loc = 'upper left')
plt.show()

