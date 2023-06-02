"""Plot a line graph to show the population growth of a city over a period of 5 years. The population data is given below:

Year Population
2018 100000
2019 110000
2020 120000
2021 130000
2022 140000"""


# Solution 1
"""import matplotlib.pyplot as plt

years = [2018, 2019, 2020, 2021, 2022]
population = [100000, 110000, 120000, 130000, 140000]

# Creating the plot
plt.plot(years, population, marker='o')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population Growth')

# Displaying the plot
plt.show()"""

print("__________________________________________")

# Solution 2
# 3d
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

years = [2018, 2019, 2020, 2021, 2022]
population = [100000, 110000, 120000, 130000, 140000]

# Creating a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotting the population growth in 3D
ax.plot(years, population, np.zeros_like(years), marker='o')

# Adding labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Population')
ax.set_zlabel('Z')
plt.title('Population Growth in 3D')

# Displaying the plot
plt.show()

