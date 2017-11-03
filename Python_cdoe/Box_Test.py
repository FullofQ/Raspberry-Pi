import sys
import time
import serial

while 1:
    
    from firebase import firebase
    from datetime import datetime
    
    __builtins__

    str = 'TEST/'
    str2 = '1'
    int = 1234
    int2 = 1
    i = 11
    firebase = firebase.FirebaseApplication('https://ftest1-9ff35.firebaseio.com/', None)

    s_result1 = "A"
    s_result2 = "A"
    s_result3 = "A"
    s_result4 = "A"
    s_result5 = "A"

    s_year = "B"
    s_month = "B"
    s_day = "B"
    s_hour = "B"
    s_minute = "B"
    
    ser = serial.Serial(
        port = '/dev/serial0',
        baudrate = 115200,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS,
        timeout = 1
        )
    
    while cmp(s_result1,s_year) != 0 or cmp(s_result2,s_month) != 0 or cmp(s_result3,s_day) != 0 or cmp(s_result4,s_hour) != 0 or cmp(s_result5,s_minute) != 0 :
        
        result1 = firebase.get('/USER/'+str,'Year')
        result2 = firebase.get('/USER/'+str,'Month')
        result3 = firebase.get('/USER/'+str,'Date')
        result4 = firebase.get('/USER/'+str,'Hour')
        result5 = firebase.get('/USER/'+str,'Min')
        result6 = firebase.get('/USER/'+str,'Num')
        print "Fail"
       
        s_result1 = __builtins__.str(result1)
        s_result2 = __builtins__.str(result2)
        s_result3 = __builtins__.str(result3)
        s_result4 = __builtins__.str(result4)
        s_result5 = __builtins__.str(result5)
        
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute
        
        s_year = __builtins__.str(year)
        s_month = __builtins__.str(month)
        s_day = __builtins__.str(day)
        s_hour = __builtins__.str(hour)
        s_minute = __builtins__.str(minute)
        
        print s_result5
        print s_minute
        
    print "Sucess"
    Num = hex(result6)
    Fiveminute = result5 + 1
    Sixminute = result5 + 2
    ser.write(Num)
    time.sleep(1)
    minute = now.minute
    
    while Fiveminute != minute:
        print "Waiting..."
        now = datetime.now()
        minute = now.minute
        result5 = firebase.get('/USER/'+str,'Min')
        Fiveminute = result5 + 1
        if Fiveminute == 60:
            Fiveminute = 0
        print minute
        print Fiveminute
        time.sleep(1)
    
    print "One minute END..."
    now = datetime.now()
    minute = now.minute
        
    while Sixminute != minute:
        print "Wating Recieve..."
        now = datetime.now()
        minute = now.minute
	result5 = firebase.get('/USER/'+str,'Min')
        Sixminute = result5 + 2
        if Sixminute == 60:
            Sixminute = 0
        elif Sixminute == 61:
            Sixminute = 1
        x = ser.read(100)
        time.sleep(1)
        print x
        alarm = __builtins__.str(x)
        y = "1"
        if cmp(alarm,y) == 1:
            print "Got it"
            Alarm = firebase.patch('/USER/'+str,{'Alarm':9})
        else:
            print "Don't Got it"