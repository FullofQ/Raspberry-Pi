import RPi.GPIO as GPIO
import time
# BOARD Number Method,Based Pin Number
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM) #Set the mode to represent the numbering scheme you prefer
GPIO.cleanup() #Return all channels you have used back to inputs
GPIO.setwarnings(False)
#Output mode
GPIO.setup(17,GPIO.OUT)

while True:
    GPIO.output(17,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(17,GPIO.LOW)
    time.sleep(1)