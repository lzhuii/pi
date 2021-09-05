# encoding == utf-8
import RPi.GPIO as GPIO
import time

touch_key = 14

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(touch_key, GPIO.IN)
    try:
        while True:
            touch_state = GPIO.input(touch_key)
            print(touch_state)
    except:
        GPIO.cleanup()
