''' Drag race code.
press the start button to start the count down.
Counts down from 5 and then forward full speed for 5 seconds.

'''
#import required libraries
import RPi.GPIO as GPIO
import time

PWMA =	36  #left side
PWMB =	33  #right side
AIN1 =	40
AIN2 =	38
BIN1 =	37
BIN2 =	35
PB_PIN = 24


print("Initializing the GPIO ports supporting drive ops.")
# Configure GPIO setting
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(PB_PIN, GPIO.IN)

# Set specific pins as output
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

GPIO.output(AIN1, False)
GPIO.output(AIN2, False)
GPIO.output(BIN1, False)
GPIO.output(BIN2, False)

GPIO.output(PWMA, False)
GPIO.output(PWMB, False)



print("Waiting for push.", end="")

push = False
while not push:
    push = not GPIO.input(PB_PIN)
    print(".", end="")
    time.sleep(.5)

print()
count = 5
while count > 0:
    print(count)
    count = count - 1
    time.sleep(1)    

print()
print("Go!")
print("Going forward")

#forward
GPIO.output(PWMA, True)
GPIO.output(PWMB, True)
time.sleep(5)
GPIO.output(PWMA, False)
GPIO.output(PWMB, False)

stop()
print("Done")


