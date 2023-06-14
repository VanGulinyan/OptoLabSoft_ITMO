#!/usr/bin/env python
# coding: utf-8

# In[12]:
# importing modules

import serial, time
import numpy as np
import matplotlib.pyplot as plt
import antaus as ant

# In[13]:

# Connecting and calibrating piezo stage
com_port = 'COM8' # piezo stage comport

with serial.Serial(port=com_port, baudrate=19200, xonxoff=True) as ser:
    command = 'setk,0,1\r' # set x-axis to closed loop in remote mode
    ser.write(command.encode()) #x
    command = 'setk,1,1\r' # set y-axis to closed loop in remote mode
    ser.write(command.encode()) #y
    command = 'setk,2,1\r' # set z-axis to closed loop in remote mode
    ser.write(command.encode()) #z

# preplot
# In[13]:

n = 30 # number of points
a = 5 # period in um
m = 10 # number of circele in x-axis
k = 10 # number of circele in y-axis
r = [0.800, 0.800, 0.800, 0.800, 0.800, 0.800, 0.800, 0.800, 0.800, 0.800] # radius in um
theta = np.linspace(0,2*np.pi, n) # angle setting from 0 to 2 pi
z = 1 # z-axis levels in um

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
# print(full_list)

# In[14]:
# TEST
# ant.CONTROL(['POWER_TRIM', 20])
# power=5
# freq_div = 99999
# aq_time = 0.1 #s
#
# ant.CONTROL(['POWER_TRIM', power])
# ant.CONTROL(['OUT_DIVIDER', freq_div])
# In[15]:


# Scanning
power = 5 # power trim
freq_div = 1 # out freq divider
aq_time = 0.1 # timeout, should be 0.1s or more

ant.CONTROL(['POWER_TRIM', power])
ant.CONTROL(['OUT_DIVIDER', freq_div])
for i in range(len(full_list)):
    with serial.Serial(port=com_port, baudrate=19200, xonxoff=True) as ser:
        ser.write(('set,0,'+str(full_list[i][0][0])+'\r').encode())
        ser.write(('set,1,'+str(full_list[i][0][1])+'\r').encode())
    time.sleep(aq_time)

    ant.CONTROL(['SHUTTER', 1])
    ant.CONTROL(['STATE'])

    with serial.Serial(port=com_port, baudrate=19200, xonxoff=True) as ser:
        for point in full_list[i]:
            command = 'set,0,'+str(point[0])+'\r'
            ser.write(command.encode())
            command = 'set,1,'+str(point[1])+'\r'
            ser.write(command.encode())
            time.sleep(aq_time)

    ant.CONTROL(['SHUTTER', 0])
    ant.CONTROL(['STATE'])

# In[14]:  

# In[ ]:




