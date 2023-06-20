#importing required libraries
import serial, time
import numpy as np
import matplotlib.pyplot as plt

#Callibration and Remote Control mode activation
com_port = 'COM8' #change to device COM-Port
with serial.Serial(port=com_port, baudrate=19200, xonxoff=True) as ser:
    command = 'setk,0,1\r'    
    ser.write(command.encode()) #x
    command = 'setk,1,1\r'    
    ser.write(command.encode())
    command = 'setk,2,1\r'    
    ser.write(command.encode())

#Configuration
#Minimal step =0.001, Max coordinate = 80
aq_time = 0.1 #s
x_min= 0 #mkm
y_min = 0 #mkm
z_min  = 0 #mkm
x_max = 80 #mkm
y_max = 80 #mkm
z_max = 80 #mkm
x_step = 20 #mkm
y_step = 20 #mkm
z_step = 20 #mkm
x_list = np.arange(0,x_max+x_step,x_step)
y_list = np.arange(0,y_max+y_step,y_step)
z_list = np.arange(0,z_max+z_step, z_step)
arr_step = 1

full_list = []
for y in y_list:
    for x in x_list[::arr_step]:
        full_list.append([x,y])
    arr_step*=-1
full_list = np.array(full_list)

#Preplot
plt.figure(dpi=200, figsize=(8,6))
plt.plot(full_list[:,0], full_list[:,1],'-o')
plt.axis('equal') 
plt.show()

#Scanning
k = 0
with serial.Serial(port=com_port, baudrate=19200, xonxoff=True) as ser:
    for i in y_list:
        command = 'set,0,'+str(i)+'\r'        
        ser.write(command.encode())
        for j in x_list[::arr_step]:            
            command = 'set,1,'+str(j)+'\r'
            ser.write(command.encode())            
        time.sleep(aq_time)
        arr_step*=-1        
        command_z = 'set,2,'+str(z_list[k])+'\r'
        ser.write(command_z.encode())       
        k+=1 #changing z-coordinate for each line
arr_step=1
