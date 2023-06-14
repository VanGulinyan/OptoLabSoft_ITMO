# Coordinates Settings and "Snake" Generation
aq_time = 0.1 #s
x_min= 0 #mkm
y_min = 0 #mkm
z_min  = 0 #mkm
x_max = 80 #mkm
y_max = 80 #mkm
z_max = 10 #mkm
x_step = 20 #mkm
y_step = 20 #mkm
z_step = 1 #mkm
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

# Preplot
plt.figure(dpi=200, figsize=(8,6))
plt.plot(full_list[:,0], full_list[:,1],'-o')
plt.axis('equal') 
plt.show()
