#Antonio Diaz, TAMU, antonio.diaz.hsa@tamu.edu, Oct 18, 2019
#Code for homework, Least Squares Estimation of monomial of sin(x)*e^(-x^2)
#Ctrl alt N to run code in Visual Studio Code

import matplotlib.pyplot as plt
import numpy as np

def sin_x_exp_negx_squared(x_input):
    return np.sin(x_input)*np.exp(-x_input**2)
    
datasize_n = 12
degree_d = 10

X = np.linspace(-1,1, datasize_n)

p1 = np.polyfit(X, sin_x_exp_negx_squared(X), degree_d)
print(p1)

plt.plot(X,sin_x_exp_negx_squared(X),'o')

new_x = np.linspace(-1,1,100)
print(np.linspace(-1,1,10), np.polyval(p1, np.linspace(-1,1,10)))
plt.plot(new_x, np.polyval(p1, new_x), 'm:')
plt.show()