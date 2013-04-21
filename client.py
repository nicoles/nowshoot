import socket
import atexit
import time
import RPi.GPIO as GPIO
from subprocess import call

# ip for camera
UDP_IP = "10.1.1.39"
UDP_PORT = 5005

# setup deal
autofocus_pin = 11
shutter_pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(autofocus_pin, GPIO.OUT)
GPIO.setup(shutter_pin, GPIO.OUT)

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))


def shoot():
    GPIO.output(shutter_pin, True)
    time.sleep(1)
    GPIO.output(shutter_pin, False)


def focus():
    GPIO.output(autofocus_pin, True)
    time.sleep(1)
    GPIO.output(autofocus_pin, False)


def cleanup():
    print "cleaning up gpio"
    GPIO.cleanup()


atexit.register(cleanup())
while True:
    # set time for photo capture from message
    # take photo at time
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    message = data.split()
    if message[0] == "shoot":
        print "received message:", message
        shoot()

    elif message[0] == "sync":
        call(["ntpdate", "-u ntp.ubuntu.com"])
        print(time.clock())
