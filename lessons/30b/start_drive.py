''' Drag race code
Press the start button to start the count
down. Counts down from 5 and forward at full
speed.
'''
import time
import RPi.GPIO as GPIO

PWMA	= 36    # right side
PWMB	= 33    # left side
AIN1	= 40
AIN2	= 38
BIN1	= 37
BIN2	= 35


def init():
    print("Initializing the GPIO ports supporting drive ops.")
    # Config GPIO settings
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    # set specific GPIO pins as output
    GPIO.setup(PWMA, GPIO.OUT)
    GPIO.setup(PWMB, GPIO.OUT)
    GPIO.setup(AIN1, GPIO.OUT)
    GPIO.setup(AIN2, GPIO.OUT)
    GPIO.setup(BIN1, GPIO.OUT)
    GPIO.setup(BIN2, GPIO.OUT)

    # enable the motor controller
    GPIO.output(PWMA, True)
    GPIO.output(PWMB, True)
    stop()

def stop():
    GPIO.output(AIN1, False)
    GPIO.output(AIN2, False)
    GPIO.output(BIN1, False)
    GPIO.output(BIN2, False)

def forward():
    GPIO.output(AIN1, False)
    GPIO.output(AIN2, True)
    GPIO.output(BIN1, False)
    GPIO.output(BIN2, True)
    
def backward():
    GPIO.output(AIN1, True)
    GPIO.output(AIN2, False)
    GPIO.output(BIN1, True)
    GPIO.output(BIN2, False)

# program starts here
###########################
print("TEST DRIVE!")
print("Press start button to start!")

init()

PB_PIN = 24
GPIO.setup(PB_PIN, GPIO.IN)

push = False
while not push:
    push = not GPIO.input(PB_PIN)
    print(".", end="")
    time.sleep(.5)

print()
count = 5
while count > 0:
    print(count)
    # count = count - 1
    count -= 1
    time.sleep(1)

#GO
# GPIO.output(PWMA, True)
# GPIO.output(PWMB, True)
# time.sleep(5)
# GPIO.output(PWMA, False)
# GPIO.output(PWMB, False)
print("Go")
forward()
time.sleep(5)
stop()
print("done")
