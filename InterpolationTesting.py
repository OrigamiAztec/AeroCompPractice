#Antonio Diaz, TAMU, antonio.diaz.hsa@tamu.edu, Oct 15, 2019
#Testing out interpolation with polynomials
#Ctrl alt N to run code in Visual Studio Code

import numpy as np
import matplotlib.pyplot as plt

#Running example from http://www1.maths.leeds.ac.uk/~kersale/2600/Notes/appendix_E.pdf
X = [1, 1.3, 1.6, 1.9, 2.2]
#adding comment right here to see if it updates
Y = [.1411, -.6878, -.9962,  -.5507, .3115]
Lagrange_Terms = []


# 5 different Lagrange polynomials
def lagrange_one(x_val):
    numerator = 1
    denominator = 1
    for num in range(0, len(X)):

        if num !=0:
            numerator *= x_val - X[num]
            #print("Numerator")
            #print(x_val-X[num])
            #print("x-" + str(X[num]))

            denominator *= X[0] - X[num]
            #print("denominator")
            #print(X[0]  - X[num])
    return numerator/denominator
    #print("output")
    #print(numerator/denominator)

def lagrange_two(x_val):
    numerator = 1
    denominator = 1
    for num in range(0, len(X)):

        if num !=1:
            numerator *= x_val - X[num]
            denominator *= X[1] - X[num]
    
    return numerator/denominator

def lagrange_three(x_val):
    numerator = 1
    denominator = 1
    for num in range(0, len(X)):

        if num !=2:
            numerator *= x_val - X[num]
            denominator *= X[2] - X[num]

    return numerator/denominator


def lagrange_four(x_val):
    numerator = 1
    denominator = 1
    for num in range(0, len(X)):

        if num !=3:
            numerator *= x_val - X[num]
            denominator *= X[3] - X[num]
    return numerator/denominator

def lagrange_five(x_val):
    numerator = 1
    denominator = 1
    for num in range(0, len(X)):

        if num !=4:
            numerator *= x_val - X[num]
            denominator *= X[4] - X[num]
    return numerator/denominator

def addtoArray(x_val):
    Lagrange_Terms = [lagrange_one(x_val), lagrange_two(x_val), lagrange_three(x_val), lagrange_four(x_val), lagrange_five(x_val)]
    return Lagrange_Terms

def lagrange_sum(x_val):
    #return .1411 * lagrange_one(x_val) + -.6878 * lagrange_two(x_val) + -.9962 * lagrange_three(x_val) + -.5507 * lagrange_four(x_val) + .3115 * lagrange_five(x_val)
    total = 0
    for num in range(0, len(Y)):
        total += (Y[num] * addtoArray(x_val)[num])
    return total

def sine3x(inp):
    return inp*np.sin(3*inp)

print(lagrange_sum(1.5))
#print(Lagrange_Terms)

X2 = np.arange(0.5, 3, .05)
plt.plot(X2, lagrange_sum(X2))
plt.plot(X2, np.sin(3*X2))

plt.plot(X,Y, 'o')
plt.show()