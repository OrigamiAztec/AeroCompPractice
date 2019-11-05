#Antonio Diaz, TAMU, antonio.diaz.hsa@tamu.edu, Oct 18, 2019
#Code for testing linear and quadratic splines
#Ctrl alt N to run code in Visual Studio Code

import matplotlib.pyplot as plt
import numpy as np

def sin_x_exp_negx_squared(x_input):
    return np.sin(x_input)*np.exp(-x_input**2)
    
datasize_n = 12
import matplotlib
