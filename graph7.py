#Rule 3 :- Any polynomial grows slower than any exponential
import matplotlib.pyplot as plt
import numpy as np
#Plot n^4 and 2^n in the range 1<=n<=10
n = np.linspace(1, 20)
plt.plot(n, n**4, label = "n^4")
plt.plot(n, 2**n, label = "2^n")
plt.legend(loc='upper left')
plt.show()