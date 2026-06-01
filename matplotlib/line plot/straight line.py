# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# # Starting point
# x = 1
# y = 2
# z = 3
# # Direction vector
# dx = 2
# dy = 1
# dz = -1
# # Store points
# x_points = []
# y_points = []
# z_points = []
# # Generate points
# for t in range(5):
#     new_x = x + t * dx
#     new_y = y + t * dy
#     new_z = z + t * dz
# # Append data
#     x_points.append(new_x)
#     y_points.append(new_y)
#     z_points.append(new_z)
# # Create 3D graph
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# # Plot line 
# ax.plot(x_points, y_points, z_points,marker='o', linewidth=2)
# # Axis names
# ax.set_xlabel("X Axis")
# ax.set_ylabel("Y Axis")
# ax.set_zlabel("Z Axis")
# # Title
# ax.set_title("Straight Line in 3D")
# plt.show()



import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(0, 10, 100)
x = 1 + 2*t
y = 2 + 1*t
z = 3 - 1*t
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(x, y, z,linewidth=2)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
