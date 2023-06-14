import serial, time

# Set home coordinates
x_0 = 0
y_0 = 0
z_0 = 0

com_port = 'COM8' # check correct device COM-port!
with serial.Serial(port=com_port, baudrate=19200, xonxoff=True) as ser: # switching axes control to remote mode
    command = 'setk,0,1\r'     
    ser.write(command.encode())
    ser.write(('set,0,str(x_0)').encode()) # x-axis
    command = 'setk,1,1\r'    
    ser.write(command.encode())
    ser.write(('set,1,str(x_0)').encode()) # y-axis
    command = 'setk,2,1\r'    
    ser.write(command.encode())
    ser.write(('set,2,str(x_0)').encode()) # z-axis
    
