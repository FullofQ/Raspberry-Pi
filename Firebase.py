from firebase import firebase
import sys
str = 'TEST/'
str2 = '1'
int = 1234
int2 = 1
i = 11
firebase = firebase.FirebaseApplication('https://professor-shi.firebaseio.com/', None)
result = firebase.patch('/USER/'+str,{'num':2})
result = firebase.get('/USER/'+str,'Y')
result2 = firebase.get('/USER/'+str,'M')
result3 = firebase.get('/USER/'+str,'D')
result4 = firebase.get('/USER/'+str,'num')
print (result)
print (result2)
print (result3)
print (result4)

from datetime import datetime
now = datetime.now()

print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)