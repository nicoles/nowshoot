import RPi.GPIO as GPIO
import time

# setup gpio pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

autofocus_pin = 11
shutter_pin = 12


# clicker
def click(pin):
    GPIO.output(pin, True)
    time.sleep(1)
    GPIO.output(pin, False)


# cleanup
def cleanup():
    GPIO.cleanup()
