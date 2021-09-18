import matplotlib.pyplot as plt
import numpy as np
#Rule 4 :- Any polylogarithm grows slower than any polynomial
n = np.linspace(1,20)
plt.plot(n, n, label = "n")
plt.plot(n, np.log(n), label = "log n")
plt.legend(loc='upper left')
plt.show()