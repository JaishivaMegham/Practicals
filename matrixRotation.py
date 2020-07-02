import numpy as np
import matplotlib.pyplot as plt


def x_rotation(vector,theta):

        Xr = np.array([  [1,       0,              0        ],
                         [0,  np.cos(theta),  -np.sin(theta)],
                         [0,  np.sin(theta),   np.cos(theta)] ])

        return np.dot(Xr,vector)

def y_rotation(vector,theta):

        Yr = np.array([  [np.cos(theta), 0, np.sin(theta) ],
                         [0,             1,     0      ],
                         [-np.sin(theta),0, np.cos(theta)] ])

        return np.dot(Yr, vector)

def z_rotation(vector,theta):

        Zr = np.array([[np.cos(theta),  -np.sin(theta), 0  ],
                       [np.sin(theta),   np.cos(theta), 0  ],
                       [     0,                0,       1  ] ])

        return np.dot(Zr, vector)


fig = plt.figure()
ax = fig.gca(projection='3d')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')


v = np.array([0,0,5])
print("Vector V: " +str(v))
ax.plot(np.linspace(0,v[0]),np.linspace(0,v[1]),np.linspace(0,v[2]))

angle_to_rotate = np.radians(30)
vnew = y_rotation(v,angle_to_rotate)
print("Vector Vnew after "+str(angle_to_rotate)+" rotations is " +str(vnew))
ax.plot(np.linspace(0,vnew[0]),np.linspace(0,vnew[1]),np.linspace(0,vnew[2]))


angle_to_rotate = np.radians(30)
vnew = y_rotation(vnew,angle_to_rotate)
print("Vector Vnew after "+str(angle_to_rotate)+" rotations is " +str(vnew))
ax.plot(np.linspace(0,vnew[0]),np.linspace(0,vnew[1]),np.linspace(0,vnew[2]))

angle_to_rotate = np.radians(30)
vnew = y_rotation(vnew,angle_to_rotate)
print("Vector Vnew after "+str(angle_to_rotate)+" rotations is " +str(vnew))
ax.plot(np.linspace(0,vnew[0]),np.linspace(0,vnew[1]),np.linspace(0,vnew[2]))

angle_to_rotate = np.radians(30)
vnew = y_rotation(vnew,angle_to_rotate)
print("Vector Vnew after "+str(angle_to_rotate)+" rotations is " +str(vnew))
ax.plot(np.linspace(0,vnew[0]),np.linspace(0,vnew[1]),np.linspace(0,vnew[2]))

plt.show()

