from socket import *
from time import sleep

sockfd = socket()
sockfd.connect(('127.0.0.1', 8888))

while True:
    sleep(0.3)
    sockfd.send(b'msg')
