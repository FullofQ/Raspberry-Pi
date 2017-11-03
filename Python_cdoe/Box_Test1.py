import sys
import time
import serial

while 1:
    
    from firebase import firebase
    from datetime import datetime
    
    __builtins__

    str = 'TEST/1'
    str2 = '1'
    int = 1234
    int2 = 1
    i = 11
    
    firebase = firebase.FirebaseApplication('https://professor-shi.firebaseio.com/', None)

    #資料庫假數值，提供while判斷
    s_result1 = "A"
    s_result2 = "A"
    s_result3 = "A"
    s_result4 = "A"
    s_result5 = "A"

    #本地時間假數值，提供while判斷
    s_year = "B"
    s_month = "B"
    s_day = "B"
    s_hour = "B"
    s_minute = "B"
    
    #串列傳輸配置
    ser = serial.Serial(
        port = '/dev/serial0',
        baudrate = 115200,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS,
        timeout = 1
        )
    
    #本地時間與資料庫時間比對
    while cmp(s_result1,s_year) != 0 or cmp(s_result2,s_month) != 0 or cmp(s_result3,s_day) != 0 or cmp(s_result4,s_hour) != 0 or cmp(s_result5,s_minute) != 0 :
        
        #GET資料庫資料
        result = firebase.patch('/USER/'+str,{'num':2})
        result = firebase.get('/USER/'+str,'Alarm')
        result2 = firebase.get('/USER/'+str,'Date')
        result3 = firebase.get('/USER/'+str,'Hour')
        result4 = firebase.get('/USER/'+str,'Item')
        result5 = firebase.get('/USER/'+str,'Min')
        result6 = firebase.get('/USER/'+str,'Num')
        print "Fail"
        
        #將資料庫int轉換為字串
        s_result2 = __builtins__.str(result2)
        s_result3 = __builtins__.str(result3)
        s_result4 = __builtins__.str(result4)
        s_result5 = __builtins__.str(result5)
        
        #本地時間函數
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute
        
        #本地時間int轉換為字串
        s_year = __builtins__.str(year)
        s_month = __builtins__.str(month)
        s_day = __builtins__.str(day)
        s_hour = __builtins__.str(hour)
        s_minute = __builtins__.str(minute)
        
        """
        print s_result5
        print type(s_result5)
        print s_minute
        x = cmp(s_result5,s_minute)
        print x
        """
    
    #比對成功，本地時間與使用者時間吻合
    print "Sucess"
    
    #傳送設定數量給2530
    ser.write(Num)
    
    #給予警報的時段，總共兩分鐘
    #兩分鐘意義在於，2530的警報會響1分20秒
    Oneminute = result5 + 1
    Twominute = result5 + 2
    
    time.sleep(1)
    minute = now.minute
    
    #第1分鐘開始
    while Oneminute != minute:
    
        print "Waiting..."
        now = datetime.now()
        minute = now.minute
        result5 = firebase.get('/USER/','Min')
        Oneminute = result5 + 1
        
        #避免整點出現的Bug，強制轉換為0
        if Oneminute == 60:
            Oneminute = 0
        
        print minute
        print Oneminute
        time.sleep(1)
    
    #第1分鐘結束
    print "One minute END..."
    
    
    now = datetime.now()
    minute = now.minute
    
    #第2分鐘開始
    while Twominute != minute:
        print "Wating Recieve..."
        now = datetime.now()
        minute = now.minute
        result5 = firebase.get('/USER/','Min')
        Twominute = result5 + 2
        
        #避免整點出現的Bug，強制轉換為0
        if Twominute == 60:
            Twominute = 0
        elif Twominute == 61:
            Twominute = 1
            
        #接收2530回報的未取藥資料
        x = ser.read(100)
        time.sleep(1)
        print x
        alarm = __builtins__.str(x)
        print alarm
        
        #給予Alarm對比的假資料
        y = "1"
        

        if cmp(alarm,y) == 1:   #判斷為1，正確警報值，傳值到Firebase Alarm欄位
            print "Got it"
            Alarm = firebase.patch('/USER/',{'Alarm':10})
        else:                   #判斷不為1，錯誤警報值
            print "Don't Got it"