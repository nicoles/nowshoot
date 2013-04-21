import RPi.GPIO as GPIO
import time

autofocus_pin = 11
shutter_pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(autofocus_pin, GPIO.OUT)
GPIO.setup(shutter_pin, GPIO.OUT)


def shoot():
    GPIO.output(shutter_pin, True)
    time.sleep(1)
    GPIO.output(shutter_pin, False)


def focus():
    GPIO.output(autofocus_pin, True)
    time.sleep(1)
    GPIO.output(autofocus_pin, False)


def cleanup():
    GPIO.cleanup()
