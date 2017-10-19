from firebase import firebase
from datetime import datetime
now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute

import sys
str = 'TEST/'
str2 = '1'
int = 1234
int2 = 1
i = 11
now = datetime.now()
firebase = firebase.FirebaseApplication('https://professor-shi.firebaseio.com/', None)
result = firebase.patch('/USER/'+str,{'num':2})
result1 = firebase.get('/USER/'+str,'Y')
result2 = firebase.get('/USER/'+str,'M')
result3 = firebase.get('/USER/'+str,'D')
result4 = firebase.get('/USER/'+str,'num')
result5 = firebase.get('/USER/'+str,'H')
result6 = firebase.get('/USER/'+str,'Min')
amountofmedicine = hex(result4)

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

if (cmp(result1,year) == 0 and cmp(result2,month) == 0):ser.write(amountofmedicine)
else:print "Fail"

"""
while 1:
    
    if (cmp(result1,year) == 0 and cmp(result2,month) == 0 and  cmp(result3,day) == 0 and cmp(result5,hour) == 0 and cmp(result6,minute) == 0):ser.write(amountofmedicine)
    else:print "Fail"
    time.sleep(1)
"""