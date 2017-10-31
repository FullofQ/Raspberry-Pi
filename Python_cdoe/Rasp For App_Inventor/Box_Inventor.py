import sys
import time
import serial

while 1:

    #串列傳輸宣告
    ser = serial.Serial(
        port = '/dev/serial0',
        baudrate = 115200,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS,
        timeout = 1
        )

    #Firebase函數
    from firebase import firebase
    from datetime import datetime
    
    #內建函數
    __builtins__
    
    #Firebase網址
    firebase = firebase.FirebaseApplication('https://test-41c36.firebaseio.com/', None)
    
  
    number = firebase.get('/USER/','Num')
    print type(number)
    
    # unicode 轉換
    s_number = __builtins__.str(number)
    i_number = int(s_number)
    h_number = hex(i_number)
    print s_number
    a = 0
        
  
  
    #判斷i_number是否為0
    while a == i_number:
    
        number = firebase.get('/USER/','Num')
        s_number = __builtins__.str(number)
        i_number = int(s_number)
        h_number = hex(i_number)
        print "Num_Zero"
    
    
    print h_number
    print "Sent"
    
    #由UART傳送值給CC2530
    ser.write(h_number)
    time.sleep(1)
    
    #將Firebase的Num重製為0
    Clear_Number = firebase.patch('/USER/',{'Num':"0"})
    
    #樹梅派本地時間
    now = datetime.now()
    minute = now.minute
    
    #延遲時間
    Oneminute = minute + 1
    Twominute = minute + 2
    
    while Oneminute != minute:
        print "Wating ..."
        now = datetime.now()
        minute = now.minute
        if Oneminute == 60:
            Oneminute = 0
        print minute
        print Oneminute
        time.sleep(1)
    
    print "Oneminute End"
    now = datetime.now()
    minute = now.minute
    
    while Twominute != minute:
    
        print "Waiting..."
        now = datetime.now()
        minute = now.minute
        
        if Twominute == 60:
            Twominute = 0
        elif Twominute == 60:
            Twominute = 0
            
        x = ser.read(100)
        time.sleep(1)
        print x
        
        alarm = __builtins__.str(x)
        print alarm
        y = "1"
        if cmp(alarm,y) == 1:
            print "Got it"
            Alarm = firebase.patch('/USER/',{'Alarm':"1"})
        else:
            print "Don't Got it"
        