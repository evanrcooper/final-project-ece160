#!/usr/bin/python3
"""
Uno game client software
Takes input from server. 
"""

from twisted.internet.protocol import Protocol, ClientFactory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

import signal
import time

WAITSIG = b"__WAIT__"
QUERSIG = b"__QUERY__"
SURESIG = b"__SURE__"

class Player(LineReceiver):
    def __init__(self):
        self.state = "QUERIED" #<----- IMPORTANT, we immediately query for username

    def dataReceived(self, line):
        """
        #does a check to see if the server sent a call to action
        if QUERSIG in line: 
            self.state == "QUERIED" 
            self.sendLine(b"SURE.")
            return
        #does a check to see if the server told it to shut up
        if WAITSIG in line:
            self.state = "WAITING"
            self.sendLine(SURESIG)
            return
        """
        if self.state == "QUERIED":
            self.handle_QUERIED(line) #<--- send a response
        else:
            self.handle_WAITING(line) #<--- observe
    """
    There are 2 states a client can exist as:
    WAITING - Waiting to deliver input. Exists to receive input
        from the server. Should not be able to send anything
    QUERIED - Has to deliver input. This could be a username, a
        move to play, or some kind of choice.

    After the game starts:
    SERVER: Queries player 1. This is NOT PRINTED TO THE USER
    CLIENT1: responds with an "ok". state is set to queried. waits
    SERVER: Sends what the user should see
    CLIENT1: Prints out, waits for the user to send a response.
    SERVER: checks if legal. assuming all is well, queries player 2.
        if not, queries player 1. Return to start and run through again
    CLIENT2: rinse and repeat
    """

    def handle_WAITING(self, line):
        if QUERSIG.decode() in line.decode():
            self.state = "QUERIED"
            self.sendLine(SURESIG)
            return
        print(line.decode())
        return

    def handle_QUERIED(self, line):
        #prints the query
        print(line.decode())
        #waits for the user to enter some funny junk
        response = input("Input: ")
        self.sendLine(response.encode())
        #sets state to WAITING
        self.state = "WAITING"
        
        return


class PlayerFactory(ClientFactory):
    def startedConnecting(self, connector):
        print("Attempting to connect...")

    def buildProtocol(self, addr):
        print("Connection Established!")
        return Player() #sets up i/o

    def clientConnectionLost(self, connector, reason):
        printToLog(f"Lost connection :(\nReason: {reason.getErrorMessage()}")
        reactor.stop()

    def clientConnectionFailed(self, connector, reason):
        printToLog(f"Unable to connect :(\nReason: {reason.getErrorMessage()}")
        reactor.stop()

#manages log, saves latest only
def printToLog(s: str, end = "\n", st = "LOG"):
    toAppend = f"{st}: {s}{end}"
    print(toAppend)
    #print to file

    return

#manages ^C input & other signals
#https://code-maven.com/catch-control-c-in-python
def handler(signum, frame): 
    reactor.stop()
    exit("Clicked ^C")


host = input("Server Hostname: ")
port = 8123

signal.signal(signal.SIGINT, handler)

reactor.connectTCP(host, port, PlayerFactory())
reactor.run()


