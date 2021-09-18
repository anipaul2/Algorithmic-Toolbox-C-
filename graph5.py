import matplotlib.pyplot as plt
import numpy as np

#Rule 1:- Multiplicative constants can be omitted.
n = np.linspace(1,100)
plt.plot(n, (7*n*n+6*n+5)/(n*n))
plt.show()