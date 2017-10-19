#!/usr/bin/env python
 
import time
import serial
 
ser = serial.Serial(
    port = '/dev/serial0',
    baudrate = 115200,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 1
    )
counter = 0
 
result = 1
hexresult = hex(result)
 
while 1:
    #command = b"\x01"
    ser.write(hexresult)
    time.sleep(1)