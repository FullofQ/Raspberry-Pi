import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) #Set the mode to represent the numbering scheme you prefer
GPIO.cleanup() #Return all channels you have used back to inputs
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
print "Light on"
GPIO.output(17,GPIO.HIGH)
GPIO.output(27,GPIO.HIGH)
