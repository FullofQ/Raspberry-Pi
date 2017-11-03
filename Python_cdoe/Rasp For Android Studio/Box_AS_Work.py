import sys
import time
import serial

while 1:
    
    from firebase import firebase
    from datetime import datetime
    
    __builtins__

    str = 'TEST/1'
    str2 = '1'
    str3 = 'Record'
    int = 1234
    int2 = 1
    i = 11
    
    firebase = firebase.FirebaseApplication('https://professor-shi.firebaseio.com/', None)

    #Fake Data
    ss_date = "A"
    ss_hour = "A"
    ss_minute = "A"
    
    #Fake Data
    s_date = "B"
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
    
 
    while cmp(ss_hour,s_hour) != 0 or cmp(ss_minute,s_minute) != 0 :
        
        
        result = firebase.get('/USER/'+str,'Alram')
        result2 = firebase.get('/USER/'+str,'Date')
        result3 = firebase.get('/USER/'+str,'Hour')
        result4 = firebase.get('/USER/'+str,'Item')
        result5 = firebase.get('/USER/'+str,'Min')
        result6 = firebase.get('/USER/'+str,'Num')
        print "Fail"
        
        ss_date = result2.encode('utf-8')
        ss_hour = __builtins__.str(result3)
        ss_item = result4.encode('utf-8')
        ss_minute = __builtins__.str(result5)
        ss_num = __builtins__.str(result6)
        ss_all = ss_date+ss_hour+ss_item+ss_minute+ss_num
        print ss_all
        
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
        s_date = s_year+s_month+s_day
        
    print "Sucess"
    
    #Fake data
    #result6 = firebase.get('/USER/'+str,'Num')
    
    Num = hex(result6)
    print Num
    ser.write(Num)
    time.sleep(1)
    
    #Fake  data
    #result5 = firebase.get('/USER/'+str,'Min')
    
    Oneminute = result5 + 1
    Twominute = result5 + 2
    
    # Fake data
    Wnow = datetime.now()
    
    minute = now.minute
  
    print "Patch Sucess"

    while Oneminute != minute:
    
        print "Waiting..."
        now = datetime.now()
        minute = now.minute
        result5 = firebase.get('/USER/'+str,'Min')
        
     
        if Oneminute == 60:
            Oneminute = 0
        
        print minute
        print Oneminute
        time.sleep(1)
        
        takemedicine = ser.read(100)
        time.sleep(1)
        Y_alarm = __builtins__.str(takemedicine)
        y = "1"
        
        if cmp(Y_alarm,y) == 1:
    
            firebase.patch('/USER/'+str,{'Alram':"YES"})
            print "Have taked a medicine"
            result = firebase.get('/USER/'+str,'Alram')
            print result
            

    print "One minute END..."
    
    
    now = datetime.now()
    minute = now.minute

    while Twominute != minute:
        print "Wating Recieve..."
        now = datetime.now()
        minute = now.minute
        result5 = firebase.get('/USER/'+str,'Min')
    
        if Twominute == 60:
            Twominute = 0
        elif Twominute == 61:
            Twominute = 1
            
        takemedicine = ser.read(100)
        time.sleep(1)
        Y_alarm = __builtins__.str(takemedicine)
        y = "1"
    
        if cmp(Y_alarm,y) == 1:
    
            firebase.patch('/USER/'+str,{'Alarm':"YES"})
            print "Have taked a medicine"
            result = firebase.get('/USER/'+str,'Alram')
            print result
    
        x = ser.read(100)
        time.sleep(1)
        print x
        N_alarm = __builtins__.str(x)
        print N_alarm
        
        y = "2"
        

        if cmp(N_alarm,y) == 1:  
            print "Got it"
            firebase.patch('/USER/'+str,{'Alram':"NO"})
            result = firebase.get('/USER/'+str,'Alram')
            print result
            
        else:                  
            print "Don't Got it"