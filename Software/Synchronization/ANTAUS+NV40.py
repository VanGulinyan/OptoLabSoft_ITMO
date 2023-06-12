#!/usr/bin/env python
# coding: utf-8

# In[12]:


import serial, time
import numpy as np
import matplotlib.pyplot as plt
import antaus as ANTAUS


# In[13]:


com_port = 'COM8'

with serial.Serial(port=com_port, baudrate=19200, xonxoff=True) as ser:
    command = 'setk,0,1\r'
    ser.write(command.encode()) #x
    command = 'setk,1,1\r'
    ser.write(command.encode()) #y
    command = 'setk,2,1\r'
    ser.write(command.encode()) #z

# preplot

n = 30 # number of points
r = [0.300, 0.400, 0.500] # radius in um
theta = np.linspace(0,2*np.pi, n)



#array of elements 
a = [1, 1.1, 1.2] # period in um
m = 3 # number of circele in x-axis
k = 3 # number of circele in y-axis

full_list = [] #list of coordinates
step_dir = 1
for j in range(k):
  x_0 = r[0]
  y_0 = r[0]
  x_list = r[j] * np.cos(theta)+x_0
  y_list = r[j] * np.sin(theta)+y_0  
  for i in np.linspace(0,m,m)[::step_dir]:
      x_element = x_list + i*a[0]
      y_element = y_list + j*a[j]
      plt.plot(x_element,y_element, '-o')
      full_list.append(np.asarray([x_element,y_element]).T)
  step_dir *=-1

plt.title("preview circle")
plt.xlabel("$x, \mu m$")
plt.ylabel("$y, \mu m$")
plt.axis('equal')
plt.show()
full_list = np.asarray(full_list)


# In[14]:


# Scanning
aq_time = 0.1 #s
for i in range(len(full_list)):
    ANTAUS(['SHUTTER', 1])
    #main(['EXIT'])

    with serial.Serial(port=com_port, baudrate=19200, xonxoff=True) as ser:
        for point in full_list[i]:
            command = 'set,0,'+str(point[0])+'\r'
            ser.write(command.encode())
            command = 'set,1,'+str(point[1])+'\r'
            ser.write(command.encode())
            time.sleep(aq_time)
    
    ANTAUS(['SHUTTER', 0])
    #main(['EXIT'])

    with serial.Serial(port=com_port, baudrate=19200, xonxoff=True) as ser:
        ser.write('set,0,'+str(full_list[i][0][0])+'\r')
        ser.write('set,1,'+str(full_list[i][0][1])+'\r')


# In[ ]:





