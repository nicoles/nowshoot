import socket
import time
import RPi.GPIO as GPIO
from subprocess import call

# ip for camera
UDP_IP = "10.1.1.39"
UDP_PORT = 5005

# setup deal
autofocus_pin = 11
shutter_pin = 12
shoot_time = 0

GPIO.cleanup()
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


def update_clock():
    call("ntpdate" + " -u ntp.ubuntu.com", shell=True)

while True:
    while shoot_time > 0:
        now = time.time()
        if now > shoot_time:
            shoot()
            shoot_time = 0

    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    message = data.split()

    if message[0] == "shoot":
        shoot_time = float(message[1])
        print "recieved shoot %s" % shoot_time
        if shoot_time - time.time() > 5:
            shoot_time = 0
    elif message[0] == "sync":
        update_clock()
        print "recieved clock update"
