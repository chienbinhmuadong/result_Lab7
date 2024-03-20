from math import pi
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


x = np.linspace(-pi, pi)
y = (np.sin(2*x))/2
z = np.sin(x)

axes = plt.axes(projection = '3d')
axes.plot3D(x, y, z, color = "red")
plt.title("graph 3D")
axes.set_xlabel("x")
axes.set_ylabel("y")
axes.set_zlabel("z")

plt.show()