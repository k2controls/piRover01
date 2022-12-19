''' The code demonstrates basic motor control
using functions to define motions such as
forward, backward, left_turn, right_turn, and stop.
'''
#import required libraries
import RPi.GPIO as GPIO
import time

#create constants to represent motor controller (MC) pin numbers
PWMA = 36   #Enable for A side (high = enabled)
PWMB = 33   #Enable for B side (high = enablled)
AIN1 = 40   #right side or left?
AIN2 = 38
BIN1 = 37   #right side or left?
BIN2 = 35

#AIN1_FORWARD = True
#BIN1_FORWARD = True
RIGHT_IN1_FORWARD = False
LEFT_IN1_FORWARD = False
RIGHT_IN1 = BIN1
RIGHT_IN2 = BIN2
LEFT_IN1 = BIN1
LEFT_IN2 = BIN2
def init():
    print("Initializing the GPIO ports supporting drive ops.")
    # Configure GPIO setting
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    # Set pin MC direction pins as output
    GPIO.setup(AIN1, GPIO.OUT)
    GPIO.setup(AIN2, GPIO.OUT)
    GPIO.setup(BIN1, GPIO.OUT)
    GPIO.setup(BIN2, GPIO.OUT)

    # Turn motors off to start
    GPIO.output(AIN1, False)
    GPIO.output(BIN2, False)
    GPIO.output(AIN1, False)
    GPIO.output(BIN2, False)
    
    # Set Enable pins as output
    GPIO.setup(PWMA, GPIO.OUT)
    GPIO.setup(PWMB, GPIO.OUT)
    # Enable MC with high on enable 
    GPIO.output(PWMA, True)
    GPIO.output(PWMB, True)

def stop():
    GPIO.output(RIGHT_IN1, False)
    GPIO.output(RIGHT_IN2, False)
    GPIO.output(LEFT_IN1, False)
    GPIO.output(LEFT_IN2, False)  

def forward(sec):
    print(f"Moving forward for {sec} seconds.")
    # Make move then sleep
    # Just guessing here on right side vs left
    # Also guessing on clockwise or counterclockwise for forward
    # You'll need to adjust based on your test
    GPIO.output(RIGHT_IN1, RIGHT_IN1_FORWARD)
    GPIO.output(RIGHT_IN2, not RIGHT_IN1_FORWARD)
    GPIO.output(LEFT_IN1, LEFT_IN1_FORWARD)
    GPIO.output(LEFT_IN2, not LEFT_IN1_FORWARD)   
    #wait
    time.sleep(sec)
    #now shut down
    stop()
 

def backward(sec):
    print(f"Moving backward for {sec} seconds.")
    GPIO.output(RIGHT_IN1, not RIGHT_IN1_FORWARD)
    GPIO.output(RIGHT_IN2, RIGHT_IN1_FORWARD)
    GPIO.output(LEFT_IN1, not LEFT_IN1_FORWARD)
    GPIO.output(LEFT_IN2, LEFT_IN1_FORWARD)   
    #wait
    time.sleep(sec)
    #now shut down
    stop()

def right_turn(sec):
    #right turn by stop on right and forward on left
    print(f"Turning right for {sec} seconds.")
    GPIO.output(RIGHT_IN1, False)
    GPIO.output(RIGHT_IN2, False)
    GPIO.output(LEFT_IN1, LEFT_IN1_FORWARD)
    GPIO.output(LEFT_IN2, not LEFT_IN1_FORWARD)   
    #wait
    time.sleep(sec)
    #now shut down
    stop()

def left_turn(sec):
    #left turn by stop on left and forward on right
    print(f"Turning left for {sec} seconds.")
    GPIO.output(RIGHT_IN1, RIGHT_IN1_FORWARD)
    GPIO.output(RIGHT_IN2, not RIGHT_IN1_FORWARD)
    GPIO.output(LEFT_IN1, False)
    GPIO.output(LEFT_IN2, False)   
    #wait
    time.sleep(sec)
    #now shut down
    stop()

def right_rotate(sec):
    #completed by student
    print(f"Turning right for {sec} seconds.")
    GPIO.output(RIGHT_IN1, not RIGHT_IN1_FORWARD)
    GPIO.output(RIGHT_IN2, RIGHT_IN1_FORWARD)
    GPIO.output(LEFT_IN1, LEFT_IN1_FORWARD)
    GPIO.output(LEFT_IN2, not LEFT_IN1_FORWARD)   
    #wait
    time.sleep(sec)
    #now shut down
    stop()

def left_rotate(sec):
    #completed by student
    print(f"Turning left for {sec} seconds.")
    GPIO.output(RIGHT_IN1, RIGHT_IN1_FORWARD)
    GPIO.output(RIGHT_IN2, not RIGHT_IN1_FORWARD)
    GPIO.output(LEFT_IN1, not LEFT_IN1_FORWARD)
    GPIO.output(LEFT_IN2, LEFT_IN1_FORWARD)   
    #wait
    time.sleep(sec)
    #now shut down
    stop()

#program starts here
command = ""
init()
print("Welcome to user drive.")
print("Valid commands are Forward, Backward, Left, Right, and Exit.")
while command != "EXIT"
    user_entry = input("Please enter a command: ")
    command = user_entry.upper()
    if command == "FORWARD"
        forward(2)

print("Done")
GPIO.cleanup()
