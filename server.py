import requests

server_list = ['192.168.0.1']

for server_ip in server_list:
    requests.get('%s:5000/shoot' % server_ip)
