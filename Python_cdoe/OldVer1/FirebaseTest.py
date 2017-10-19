from firebase import firebase
import sys
str = 'KEVIN/'
str2 = '1'
int = 1234
int2 = 1
i = 11
firebase = firebase.FirebaseApplication('https://android-40673.firebaseio.com/', None)
result = firebase.get('/USER/'+str,'account')
print (result)