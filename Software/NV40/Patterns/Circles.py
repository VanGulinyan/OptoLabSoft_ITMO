import matplotlib.pyplot as plt
import numpy as np

n = 30 # number of points
a = 5 # period in um
m = 10 # number of circele in x-axis
k = 10 # number of circele in y-axis
r = [0.800, 0.800, 0.800, 0.800, 0.800, 0.800, 0.800, 0.800, 0.800, 0.800] # radius in um
theta = np.linspace(0,2*np.pi, n) # angle setting from 0 to 2 pi

full_list = [] #list of coordinates
step_dir = 1

#circles XY axes
for j in range(k):
  x_0 = r[0]
  y_0 = r[0]
  x_list = r[j] * np.cos(theta)+x_0
  y_list = r[j] * np.sin(theta)+y_0  
  for i in np.linspace(0,m,m)[::step_dir]:
      x_element = x_list + i*a
      y_element = y_list + j*a
      plt.plot(x_element,y_element, '-o')
      full_list.append(np.asarray([x_element, y_element, z]).T)
  step_dir *=-1

plt.title("preview circle")
plt.xlabel("$x, \mu m$")
plt.ylabel("$y, \mu m$")
plt.axis('equal')
plt.show()
full_list = np.asarray(full_list)
