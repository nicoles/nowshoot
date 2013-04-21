import RPi.GPIO as GPIO
import time
import socket

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


# set up listening socket
broadcast_host = '255.255.255.255'
broadcast_port = 54545

broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    broadcast_socket.bind((broadcast_host, broadcast_port))
except:
    print "failed to bind"
    broadcast_socket.close()

message = ''
broadcast_socket.listen(message)
while message:
    print "got a message"
    click(12)

GPIO.cleanup()
