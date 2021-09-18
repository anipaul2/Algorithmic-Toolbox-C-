#Another way of showing graph3.py is :-
import matplotlib.pyplot as plt
import numpy as np
n = np.linspace(1,100)
plt.plot(n, (7*n*n+6*n+5)/(7*n*n))
plt.show()