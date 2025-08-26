'''piRover blink-beep solution
Keith E. Kelly
9/23/23
'''
import time
import RPi.GPIO as GPIO

LED_PIN = 13
BUZZER_PIN = 24

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

while True:
    print("LED off, Buzzer off")
    GPIO.output(LED_PIN, False)
    GPIO.output(BUZZER_PIN, True)
    time.sleep(1)
    print("LED on, Buzzer on")
    GPIO.output(LED_PIN, True)
    GPIO.output(BUZZER_PIN, False)
    time.sleep(1)
  