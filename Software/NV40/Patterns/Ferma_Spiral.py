import matplotlib.pyplot as plt
import numpy as np
n = 8 # n*pi - finish angle
theta = np.arange(0, n*np.pi, 0.1)
a = 1
b = 0.03

full_list = []
for dt in np.arange(0, 2*np.pi, np.pi/2.0):
    x = np.sign(a)*np.abs(a)*(theta**0.5)*np.cos(theta)
    y = np.sign(a)*np.abs(a)*(theta**0.5)*np.sin(theta)
    x1 = -1*np.sign(a)*np.abs(a)*(theta**0.5)*np.cos(theta)
    y1 = -1*np.sign(a)*np.abs(a)*(theta**0.5)*np.sin(theta)
full_list.append([x,y])
full_list.append([x1,y1])
full_list = np.array(full_list)

# Preplot
plt.figure(dpi=200, figsize=(8,6))
plt.plot(full_list[:,0], full_list[:,1],'-o', markersize=2, linewidth=0.1)
plt.axis('equal') 
plt.show()
