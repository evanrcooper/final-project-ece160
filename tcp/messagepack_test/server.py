#!/usr/bin/python3

import socket
from threading import *
import time

#import addressbook_pb2
import sys
import struct

import itertools

#important for talking to C
import ctypes as ct

#msgpack
import msgpack

#https://stackoverflow.com/questions/66340519/how-do-i-pass-a-multiline-string-from-python-to-c-using-ctypes 
#https://stackoverflow.com/questions/48822543/reading-a-c-struct-via-sockets-into-python
class Card(ct.Structure):
    fields = {
        ("c", ct.POINTER(ct.c_char)),
        ("t", ct.c_int),
    }

msg = input("input color: ").encode()
msg2 = int(input("input number: "))

toSend = msgpack.packb([msg, msg2], use_bin_type=False)

s = socket.create_server(('localhost', 12345)) #host, port, this is a convenience function which auto does an internet ipv4 socket

#Client Class.
#this takes care of client threads for multiple connections.

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while True:
            self.sock.send((toSend))
            print("sent message to ")
            time.sleep(10)
        #self.sock.close()

#main
s.listen(5)
print("Started and listening.")
print(toSend)
i = 0
while True:
    conn, addr = s.accept()
    print("Connection made!")
    if i < 5:
        client(conn, addr)
        i = i + 1
    else:
        print("fuck off nonce")
