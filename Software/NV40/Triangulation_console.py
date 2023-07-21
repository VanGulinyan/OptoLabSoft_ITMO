import numpy as np
coor1 = [int(x) for x in (input('Введите значения координат первой точки: ')).split()]
coor2 = [int(x) for x in (input('Введите значения координат второй точки: ')).split()]
coor3 = [int(x) for x in (input('Введите значения координат третьей точки: ')).split()]

M = np.array([[coor1[0], coor1[1], 1], [coor2[0], coor2[1], 1], [coor3[0], coor3[1], 1]])
v = np.array([coor1[2], coor2[2], coor3[2]])

coef = np.linalg.solve(M, v)
print(coef)

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

arr_step = 1
full_list = []
for y in y_list:
    for x in x_list[::arr_step]:
        full_list.append([x,y, round(x*coef[0] + y*coef[1] + coef[2], 3)])
    arr_step*=-1
full_list = np.array(full_list)
print(full_list)
