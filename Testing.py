#ctrl alt N to run code in Visual Studio Code
import numpy as np
import matplotlib.pyplot as plt

X = [0, 1, 2, 3, 4]
Y = [0, 1, 2, 3, 4]

plt.plot(X, Y)
plt.show()

for num in range(0, 10):
    print(num)

def concat(*args, sep = "/"):
    return sep.join(args)

string_input = input("Enter numbers to join: ")    
print(concat(string_input))