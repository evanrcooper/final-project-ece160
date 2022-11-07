#!/usr/bin/python3

import socket
import time

host = 'localhost'
port = 12345


print("Attempting to find valid UNO game...")
while True:
    try:
        s = socket.create_connection(('localhost', 12345))
    except:
        time.sleep(3)
    else:
        print("Connection Established!")
        break
    
while True:
    foobar = s.recv(1024).decode()
    print(foobar)
    foobar = int(s.recv(1024).decode())
    print(foobar)


