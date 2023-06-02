"""Bonus(Bar Plot):
Create a bar chart to compare the sales performance of different products for a company. The sales data for each product is given below:

Product A: $5000
Product B: $8000
Product C: $3000
Product D: $6000
Hint:
To solve this exercise, you'll need to import the Matplotlib library and use the bar function to create the bar chart.
define two lists, products and sales, to store the product names and sales data, respectively.
use the bar function to create a bar chart
pass products as the x-axis values and sales as the y-axis values.
add labels to the x-axis and y-axis using the xlabel and ylabel functions, respectively.
set the title of the chart using the title function.
 display the chart using the show function."""

 # Solution 1
"""import matplotlib.pyplot as plt

products = ['Product A', 'Product B', 'Product C', 'Product D']
sales = [5000, 8000, 3000, 6000]

# Creating the bar chart
plt.bar(products, sales)

# Adding labels and title
plt.xlabel('Product')
plt.ylabel('Sales')
plt.title('Sales Performance')

# Displaying the chart
plt.show()"""

print("____________________________________________")

# Solution 1 colours
"""import matplotlib.pyplot as plt
import numpy as np

products = ['Product A', 'Product B', 'Product C', 'Product D']
sales = [5000, 8000, 3000, 6000]

# Generating a color map
color_map = plt.cm.get_cmap('Set3')

# Creating the bar chart
plt.bar(products, sales, color=color_map(np.arange(len(products))))

# Adding labels and title
plt.xlabel('Product')
plt.ylabel('Sales')
plt.title('Sales Performance')

# Displaying the chart
plt.show()"""

print("____________________________________________________")

# Solution 2
# 3D
"""import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

products = ['Product A', 'Product B', 'Product C', 'Product D']
sales = [5000, 8000, 3000, 6000]

# Generating coordinates for the bars
x_pos = np.arange(len(products))
y_pos = np.zeros(len(products))
z_pos = np.zeros(len(products))
width = 0.5
depth = sales
height = 0

# Creating a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Creating the 3D bars
ax.bar3d(x_pos, y_pos, z_pos, width, depth, height)

# Adding labels and title
ax.set_xlabel('Product')
ax.set_ylabel('Y')
ax.set_zlabel('Sales')
plt.title('Sales Performance in 3D')

# Adding product names to the x-axis ticks
ax.set_xticks(x_pos)
ax.set_xticklabels(products)

# Displaying the chart
plt.show()"""

print("_________________________________________")

# Solution 3D colour
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

products = ['Product A', 'Product B', 'Product C', 'Product D']
sales = [5000, 8000, 3000, 6000]

# Generating coordinates for the bars
x_pos = np.arange(len(products))
y_pos = np.zeros(len(products))
z_pos = np.zeros(len(products))
width = 0.5
depth = sales

# Creating a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generating a color map
color_map = plt.cm.get_cmap('Set3')

# Creating the 3D bars with different colors
for i, d in enumerate(depth):
    ax.bar3d(x_pos[i], y_pos[i], z_pos[i], width, d, z_pos[i], color=color_map(i))

# Adding labels and title
ax.set_xlabel('Product')
ax.set_ylabel('Y')
ax.set_zlabel('Sales')
plt.title('Sales Performance in 3D')

# Adding product names to the x-axis ticks
ax.set_xticks(x_pos)
ax.set_xticklabels(products)

# Displaying the chart
plt.show()


