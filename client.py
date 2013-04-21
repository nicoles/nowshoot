import cameratasks
import socket
import atexit

# ip for camera
UDP_IP = "10.1.1.39"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

# register cleanup on exit
atexit.register(cameratasks.cleanup())

while True:
    # set time for photo capture from message
    # take photo at time
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    message = data.split()
    if message[0] == "shoot":
        print "received message:", message
        cameratasks.click(12)
