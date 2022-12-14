#!/usr/bin/python3
#https://www.devdungeon.com/content/python-catch-sigint-ctrl-c

from signal import signal, SIGUSR2
from sys import exit
from os import getpid

def handler(signum, frame):
    print("signal caught!")

signal(SIGUSR2, handler)
pid = getpid()
print(f"pid: {pid}")
print("We are live! Awaiting SIGUSR2")
while True:
    pass

