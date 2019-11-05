#Antonio Diaz, TAMU, antonio.diaz.hsa@tamu.edu, Oct 18, 2019
#Code for testing linear and quadratic splines
#Ctrl alt N to run code in Visual Studio Code

import matplotlib.pyplot as plt
import numpy as np
    
x_vals = [-1 , -.6, -.2, .2, .6, 1]
y_vals = [.038461 , .1, .5, .5, .1, .038461]

slope = (y_vals[1]-y_vals[0])/(x_vals[1]-x_vals[0])

#between x_vals[0] and x_vals[1]

print(y_vals[1])

def linear_output_one(x_input):
    y_int = y_vals[0]
    return slope*x_input + y_int - slope*x_vals[0]

x_vals_sect_one = np.arange(x_vals[0], x_vals[1], .01)
y_vals_sect_one = linear_output_one(x_vals_sect_one)

plt.plot(x_vals_sect_one, y_vals_sect_one, 'bo')
plt.plot(x_vals, y_vals, 'ro')

plt.show()