'''piRover beep solution
Keith E. Kelly
9/20/23
'''
import time
import RPi.GPIO as GPIO

BUZZER_PIN = 24

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

while True:
    print("Buzzer off")
    GPIO.output(BUZZER_PIN, True)
    time.sleep(1)
    print("turn the buzzer on")
    GPIO.output(BUZZER_PIN, False)
    time.sleep(1)
  