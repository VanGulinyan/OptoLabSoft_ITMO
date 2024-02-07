from LabOptic import * 
from draw_methods import * 
import time
import numpy as np
 
ximc_z = Ximc(1)  
ximc_x = Ximc(0)  
ximc_y = Ximc(2) #0 - x, 1 - z (вверх низ), 2 - y  
ant = Antaus()  
# ant.set_base_divider(177)  
# ant.set_freq_time(1)  
# ant.set_power_trim(40)  
 
# speed in um/s
speed_x = 10 
speed_y = 10 
speed_z = 10 

# initializing stages
ximc_y.connect() 
ximc_z.connect() 
ximc_x.connect() 
  
# setting speed and getting current coordinates
cord_x = ximc_x.get_position()  
ximc_x.set_speed(speed_x)  
cord_z = ximc_z.get_position()  
ximc_z.set_speed(speed_z)  
cord_y = ximc_y.get_position()  
ximc_y.set_speed(speed_y)  

# generation of coordinates for array
x_min= 0 #mkm  
y_min = 0 #mkm  
z_min  = 0 #mkm  
x_max = 25 #mkm  
y_max = 75 #mkm  
z_max = 25 #mkm  
x_step = 5 #mkm  
y_step = 15 #mkm  
z_step = 5 #mkm  
x_list = np.arange(int(cord_x[0]),(int(cord_x[0]))+(x_max)+x_step, x_step)  
z_list = np.arange(int(cord_z[0]),(int(cord_z[0]))+(z_max)+ z_step,z_step)  
y_list = np.arange(int(cord_y[0]),(int(cord_y[0]))+(y_max),y_step)  
 
print(x_list)  
print(z_list)  
print(y_list)  
 
# aq_time = [6, 5, 4, 3, 2]  
# power = [70, 60, 50, 40, 30, 20]  
# arr_step=1  
# k = 0  
# p = 0  
# t=0  
 
arr_step = 1  
p = 0

power = [1,2,3,4,5] # in %, array length should be equal to the number of rows
aq_time = [1,2,3,4,5] # in seconds, array length should be equal to the number of columns

for i in z_list[1:]: 
    t = 0
    # ant.set_power_trim(power[p]) # uncomment to change power in all lines
    ximc_z.move(int(i), cord_z[1]) 
    time.sleep(z_step/speed_z + 0.1)      # (расстояние между точкам / скорость) + 0.5сек 
    for j in x_list[1::arr_step]: 
        ximc_x.move(int(j), cord_x[1]) 
        time.sleep(x_step/speed_x)    # таймаут на перемещение 
        ant.schutter_open() 
        time.sleep(0.1)    # длительность открытого шаттера 
        # time.sleep(aq_time[t]) # uncomment to change aquisition time in each point
        ant.schutter_close()
        t +=1 
    ximc_x.move(cord_x[0], cord_x[1]) 
    
    time.sleep((x_max+x_step)/speed_x+0.1)  # таймаут на перемещение
    
    p += 1 
    arr_step*=1 # change to -1 if snake-like array
ant.schutter_close() 
