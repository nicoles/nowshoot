import socket
import time

# dictionary of cameras & ips in order along rail
camera_list = {1: '10.1.1.39', 2: '192.168.1.1'}

# udp port for camera
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP

# get ntp time


def shoot_all(time):
    MESSAGE = "shoot %s" % time
    for camera in camera_list:
        sock.sendto(MESSAGE, (camera_list[camera], UDP_PORT))


def sync_clocks():
    MESSAGE = "sync"
    for camera in camera_list:
        sock.sendto(MESSAGE, (camera_list[camera], UDP_PORT))


def shoot_interval():
    MESSAGE = "shoot %s"
    for camera in camera_list:
        sock.sendto(MESSAGE, (camera_list[camera], UDP_PORT))

sync_clocks()
shoot_all(time.time()+1)
