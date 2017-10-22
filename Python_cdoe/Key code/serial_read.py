import time
import serial

__builtins__
 
ser = serial.Serial(
    port = '/dev/serial0',
    baudrate = 115200,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 1
    )

while 1:
    
    x = ser.read(100)
    time.sleep(1)
    #print x
    alarm = __builtins__.str(x)
    #print dinner
    y = "1"
    if cmp(alarm,y) == 1:
        print "Recieve Sucess"
    else:
        print "Fail"
    

