from firebase import firebase
from datetime import datetime
import sys
import time
import serial

now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute

str = 'TEST/'
str2 = '1'
int = 1234
int2 = 1
i = 11

firebase = firebase.FirebaseApplication('https://professor-shi.firebaseio.com/', None)

ser = serial.Serial(
    port = '/dev/serial0',
    baudrate = 115200,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 1
    )

result1 = 0
result2 = 0
result3 = 0
result4 = 0
result5 = 0
result6 = 0

def GetFirebase():
    
    result1 = firebase.get('/USER/'+str,'Y')
    result2 = firebase.get('/USER/'+str,'M')
    result3 = firebase.get('/USER/'+str,'D')
    result4 = firebase.get('/USER/'+str,'num')
    result5 = firebase.get('/USER/'+str,'H')
    result6 = firebase.get('/USER/'+str,'Min')
	
	

while 1:

	if cmp(result1,year) != 0 and cmp(result2,month) != 0and  cmp(result3,day) != 0 and cmp(result5,hour) != 0 and cmp(result6,minute) != 0:
		
		GetFirebase()
		amountofmedicine = hex(result4)
		print "Fail"
		time.sleep(1)
	
	ser.write(amountofmedicine)
	time.sleep(1)
	
	while(minute != )




	