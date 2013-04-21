import socket

broadcast_host = '255.255.255.255'
broadcast_port = 54545
# set up socket for broadcast
broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# send test message over broadcast
message = "Click camera"
broadcast_socket.sendto(message, (broadcast_host, broadcast_port))
