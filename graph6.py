import matplotlib.pyplot as plt
import numpy as np
#Rule 2 :- Out of two polynomials, the one with larger degree grows faster
n = np.linspace(1,100)
plt.plot(n, n, label = "n")
plt.plot(n, n*n, label = "n^2")
plt.plot(n, n*n*n, label = "n^3")
plt.legend(loc = 'upper left')
plt.show()