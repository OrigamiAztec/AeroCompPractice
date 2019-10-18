#Antonio Diaz, TAMU, antonio.diaz.hsa@tamu.edu, Oct 18, 2019
#Code for homework, Least Squares Estimation of monomial of sin(x)*e^(-x^2)
#Ctrl alt N to run code in Visual Studio Code

from numpy import *
from scipy.interpolate import *

X = array([3.8462, 3.2632, 3.7149, 3.4779])
Y = array([.2726, .2274, .2315, .2637])

print(X)
print(Y)

p1 = polyfit(X, Y, 1)
print(p1)