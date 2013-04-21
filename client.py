import cameratasks
import socket
import atexit
import RPi.GPIO as GPIO

# ip for camera
UDP_IP = "10.1.1.39"
UDP_PORT = 5005

autofocus_pin = 11
shutter_pin = 12

# setup deal
GPIO.setmode(GPIO.BOARD)
GPIO.setup(autofocus_pin, GPIO.OUT)
GPIO.setup(shutter_pin, GPIO.OUT)
atexit.register(cameratasks.cleanup())
sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))


while True:
    # set time for photo capture from message
    # take photo at time
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    message = data.split()
    if message[0] == "shoot":
        print "received message:", message
        cameratasks.shoot()
