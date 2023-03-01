''' Traffic Light Simulation - Student Project
Keith E. Kelly
2/28/2022
'''
#import required libraries
import time
import RPi.GPIO as GPIO

#create constants to represent piRover LED pin numbers
RED_PIN = 15
GREEN_PIN = 13
# BLUE_PIN = 18
# push button simulates a sensor in the road
PB_PIN = 24

#create constant to represent the green, amber,and red timings for NS
NS_GREEN_DELAY = 24/2
NS_AMBER_DELAY = 3/2
NS_RED_DELAY = (66/2-NS_GREEN_DELAY-NS_AMBER_DELAY)/2

#create constant to represent the green, amber,and red timings for EW
EW_GREEN_DELAY = 27/2
EW_AMBER_DELAY = NS_AMBER_DELAY
EW_RED_DELAY = (24+9)/2

#create timing variables for green, amber, and red
green_delay = 0
amber_delay = 0
red_delay = 0 

# Configure GPIO setting
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Set specific pins as output
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
# GPIO.setup(BLUE_PIN, GPIO.OUT)
GPIO.setup(PB_PIN, GPIO.IN)


# Initialize all LEDs to OFF
GPIO.output(RED_PIN, False)
GPIO.output(GREEN_PIN, False)
# GPIO.output(BLUE_PIN, False)

# Welcome user and prompt for NS or EW simulation
print("Welcome to the traffic light simulation!")
print("This program simulates either the north_south or east-west lights. ")
print("East-west is a smart light and changes to red only if sensor is on.")
# Check user's direction input. If valid then set light timing variables
user_entry = input("Which direction would you like to simulate? NS or EW?")
direction = user_entry.upper().strip()
if direction == "NS" or direction == "EW":
    # valid entry so continue
    if direction == "NS":
        green_delay = NS_GREEN_DELAY
        amber_delay = NS_AMBER_DELAY
        red_delay = NS_RED_DELAY
        smart = False
    # elif direction == "EW":
    else:  #smart light
        green_delay = EW_GREEN_DELAY
        amber_delay = EW_AMBER_DELAY
        red_delay = EW_RED_DELAY
        smart = True        
    
    # Use a while loop initially to test light cycles
    # while True:
    #     # red on
    #     GPIO.output(RED_PIN, True)
    #     time.sleep(red_delay)
    #     GPIO.output(RED_PIN, False)
    #     # green on
    #     GPIO.output(GREEN_PIN,True)
    #     time.sleep(green_delay)
    #     # turn red and green to make amber
    #     GPIO.output(RED_PIN, True)
    #     time.sleep(amber_delay)
    #     GPIO.output(GREEN_PIN, False)   
    
    # Implement for loop as time permits
    for i in range(0,4):
        # red on
        GPIO.output(RED_PIN, True)
        time.sleep(red_delay)
        GPIO.output(RED_PIN, False)
        # green on
        GPIO.output(GREEN_PIN,True)
        # should light advance to amber?
        if smart:
            road_sensor = True
            while road_sensor:
                road_sensor = GPIO.input(PB_PIN)
                time.sleep(.5)

        time.sleep(green_delay)
        # turn red and green to make amber
        GPIO.output(RED_PIN, True)
        time.sleep(amber_delay)
        GPIO.output(GREEN_PIN, False)
    
    print("Done")

else:
    print("Sorry, invalid input. Unable to continue.")

