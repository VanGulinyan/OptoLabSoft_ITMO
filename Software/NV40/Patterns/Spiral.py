import matplotlib.pyplot as plt
import numpy as np
n = 32 # n*pi - finish angle
theta = np.arange(0, n*np.pi, 0.1)
a = 1
b = 0.03

full_list = []

for dt in np.arange(0, 2*np.pi, np.pi/2.0):

    x = a*np.cos(theta + dt)*np.exp(b*theta)
    y = a*np.sin(theta + dt)*np.exp(b*theta)

full_list.append([x,y])
full_list = np.array(full_list)

# Preplot
plt.figure(dpi=200, figsize=(8,6))
plt.plot(full_list[:,0], full_list[:,1],'-o')
plt.axis('equal') 
plt.show()
