import sys
import time
import serial

while 1:
    
    from firebase import firebase
    from datetime import datetime
    
    __builtins__

    #str = 'TEST/'
    #str2 = '1'
    int = 1234
    int2 = 1
    i = 11
    firebase = firebase.FirebaseApplication('https://test-41c36.firebaseio.com/', None)

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
        
        result1 = firebase.get('/USER/','Year')
        result2 = firebase.get('/USER/','Month')
        result3 = firebase.get('/USER/','Date')
        result4 = firebase.get('/USER/','Hour')
        result5 = firebase.get('/USER/','Min')
        result6 = firebase.get('/USER/','Num')
        print "Fail"
        
        s_result1 = __builtins__.str(result1)
        s_result2 = __builtins__.str(result2)
        s_result3 = __builtins__.str(result3)
        s_result4 = __builtins__.str(result4)
        s_result5 = __builtins__.str(result5)
        s_result6 = __builtins__.str(result6)
        
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
    Num = result6.encode('utf-8')
    ser.write(Num)
    i_result5 = result5.encode('utf-8')
    #print type(i_result5)
    print i_result5
    in_result5 = __builtins__.int(i_result5)
    # print type(in_result5)
    print in_result5
    
    Fiveminute = in_result5 + 1
    Sixminute = in_result5 + 2
    
    time.sleep(1)
    minute = now.minute
    
    while Fiveminute != minute:
        print "Waiting..."
        now = datetime.now()
        minute = now.minute
        result5 = firebase.get('/USER/','Min')
        s_result5 = __builtins__.str(result5)
        i_result5 = __builtins__.int(result5)
        Fiveminute = i_result5 + 1
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
        result5 = firebase.get('/USER/','Min')
        s_result5 = __builtins__.str(result5)
        i_result5 = __builtins__.int(result5)
        Sixminute = i_result5 + 2
        if Sixminute == 60:
            Sixminute = 0
        elif Sixminute == 61:
            Sixminute = 1
        x = ser.read(100)
        time.sleep(1)
        print x
        alarm = __builtins__.str(x)
        print alarm
        y = "1"
        if cmp(alarm,y) == 1:
            print "Got it"
            Alarm = firebase.patch('/USER/',{'Alarm':9})
        else:
            print "Don't Got it"