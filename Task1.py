"""generate  with matplotlib the following graph:
 LogN
 N
 NlogN
 N_square
 N_exp
 N!
you can calculate with a list comprehension:
N_exp =  [math.exp(ele) for ele in sizes]
for y = exp(x)
Y = [2.718281828459045, 7.38905609893065, 20.085536923187668, 54.598150033144236]
X  = [1,2,3,4]"""
print("____________________________________________________")

# Solution 1
import matplotlib.pyplot as plt
import math

sizes = [1, 2, 3, 4]

# Calculate values for the functions
logN = [math.log(ele) for ele in sizes]
N = sizes
NlogN = [ele * math.log(ele) for ele in sizes]
N_square = [ele**2 for ele in sizes]
N_exp = [math.exp(ele) for ele in sizes]
N_fact = [math.factorial(ele) for ele in sizes]

# Creating the plot
plt.plot(sizes, logN, label='Log(N)')
plt.plot(sizes, N, label='N')
plt.plot(sizes, NlogN, label='Nlog(N)')
plt.plot(sizes, N_square, label='N^2')
plt.plot(sizes, N_exp, label='N^exp')
plt.plot(sizes, N_fact, label='N!')

# Adding labels and title
plt.xlabel('N')
plt.ylabel('Function Value')
plt.title('Function Comparison')

# Adding a legend
plt.legend()

# Displaying the plot
plt.show()

print("__________________________________________")

"""# Solution 2
import matplotlib.pyplot as plt
import math

sizes = [1, 2, 3, 4]

# Calculate values for the functions using map()
logN = list(map(math.log, sizes))
N = sizes
NlogN = list(map(lambda x: x * math.log(x), sizes))
N_square = list(map(lambda x: x**2, sizes))
N_exp = list(map(math.exp, sizes))
N_fact = list(map(math.factorial, sizes))

# Creating the plot
plt.plot(sizes, logN, label='Log(N)')
plt.plot(sizes, N, label='N')
plt.plot(sizes, NlogN, label='Nlog(N)')
plt.plot(sizes, N_square, label='N^2')
plt.plot(sizes, N_exp, label='N^exp')
plt.plot(sizes, N_fact, label='N!')

# Adding labels and title
plt.xlabel('N')
plt.ylabel('Function Value')
plt.title('Function Comparison')

# Adding a legend
plt.legend()

# Displaying the plot
plt.show()
"""
print("_________________________________________________")

# Solution 3 
# 3D
"""import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

sizes = np.arange(1, 5)  # Generating x-axis values from 1 to 50

# Calculate values for the functions
logN = np.log(sizes)
N = sizes
NlogN = sizes * np.log(sizes)
N_square = sizes**2
N_exp = 2**sizes
N_fact = np.array([np.math.factorial(n) for n in sizes])

# Additional data points
Y = [2.718281828459045, 7.38905609893065, 20.085536923187668, 54.598150033144236]
X = [1, 2, 3, 4]

# Creating a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotting the functions in 3D
ax.plot(sizes, logN, N, label='Log(N)')
ax.plot(sizes, N, N, label='N')
ax.plot(sizes, NlogN, N, label='Nlog(N)')
ax.plot(sizes, N_square, N, label='N^2')
ax.plot(sizes, N_exp, N, label='N^exp')
ax.plot(sizes, N_fact, N, label='N!')
ax.plot(X, Y, X, marker='o', linestyle='', label='Additional Points')

# Adding labels and title
ax.set_xlabel('N')
ax.set_ylabel('Y')
ax.set_zlabel('Function Value')
plt.title('Function Comparison in 3D')

# Adding a legend
ax.legend()

# Displaying the plot
plt.show()"""
