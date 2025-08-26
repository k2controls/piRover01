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

def init():
    print("Initializing the GPIO ports supporting drive ops.")
    # Configure GPIO setting
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

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

    GPIO.output(PWMA, True)
    GPIO.output(PWMB, True)

def stop():
    print("Stopped.")
    GPIO.output(AIN1, False)
    GPIO.output(AIN2, False)
    GPIO.output(BIN1, False)
    GPIO.output(BIN2, False)

def forward():
    print(f"Moving forward...")
    GPIO.output(AIN1, False)
    GPIO.output(AIN2, True)
    GPIO.output(BIN1, False)
    GPIO.output(BIN2, True)

def backward():
    print(f"Moving backward....")
    GPIO.output(AIN1, True)
    GPIO.output(AIN2, False)
    GPIO.output(BIN1, True)
    GPIO.output(BIN2, False)

def right_turn():
    #right turn by stop on right and forward on left
    print(f"Turning right...")
    GPIO.output(AIN1, False)
    GPIO.output(AIN2, True)
    GPIO.output(BIN1, False)
    GPIO.output(BIN2, False)

def left_turn():
    #left turn by stop on left and forward on right
    print(f"Turning left...")
    GPIO.output(AIN1, False)
    GPIO.output(AIN2, False)
    GPIO.output(BIN1, False)
    GPIO.output(BIN2, True)

def right_rotate():
    GPIO.output(AIN1, False)
    GPIO.output(AIN2, True)
    GPIO.output(BIN1, True)
    GPIO.output(BIN2, False)

def left_rotate():
    GPIO.output(AIN1, True)
    GPIO.output(AIN2, False)
    GPIO.output(BIN1, False)
    GPIO.output(BIN2, True)


#program starts here
print("Wecome to the drag race")
print("Press the start button to go!")
print()

init()

PB_PIN = 24
GPIO.setup(PB_PIN, GPIO.IN)

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
# forward()
time.sleep(3)
stop()
print("Done")


