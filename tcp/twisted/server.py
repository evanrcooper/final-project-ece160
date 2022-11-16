#!/usr/bin/python3 

from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver

#FIX THE BOOKKEEPING
maxConnections = 4 #max amount of clients we allow
currentConnections = 0 #amount of clients connected


class Uno(LineReceiver):
    def __init__(self, players, addr):
        self.players = players #list of players
        self.addr = addr
        self.name = None
        self.state = "GETNAME"

    def connectionMade(self):
        print(f"Player joined the lobby. Info: {self.addr}")
        #currentConnections += 1
        print(f"Num of current clients: {currentConnections}")
        print(f"Waiting for more players....", end='\n\n')
        self.sendLine(b"Thanks for joining the game. Please choose an alias: ")

    def connectionLost(self, reason):
        print(f"Player {self.name} left the lobby. Info: {self.addr}")
        #currentConnections -= 1
        if self.name.encode() in self.players:
            del self.players[self.name.encode()] 
        print(self.players)

    def lineReceived(self, line): #change to switch case later
        if self.state == "GETNAME":
            self.handle_GETNAME(line)
        else:
            self.handle_AWAITING_START(line)

    def handle_GETNAME(self, name):
        if name in self.players:
            self.sendLine(b"Alias taken. choose another!")
            return
        self.name = name.decode()
        self.players[name] = self
        self.state = "AWAITING_START"
        self.sendLine(b"Thanks. Waiting for everyone to be ready....")
        self.sendLine(b"Current Lobby goes here.")
        self.sendLine(b"Options: r to change alias, q to quit.")
        print(f"{self.name} is ready!")
        return

    def handle_AWAITING_START(self, line):
        if line.decode() == "r":
            self.state = "GETNAME"
            if self.name.encode() in self.players: #redundancy
                del self.players[self.name.encode()]
            self.sendLine(b"\nNew alias?")
            print(f"Heads up. {self.name} is changing their alias.")
        return
        #print whose in the lobby
        #continually update

class unoFactory(Factory):
    def __init__(self):
        # sets up array for every player to be stuck into
        self.players = {}
    
    def buildProtocol(self, addr):
        return Uno(self.players, addr)
#https://stackoverflow.com/questions/30196186/how-to-limit-the-number-of-simultaneous-connections-in-twisted


#build mainloop later
#build exception handler later if the tcp connection fails to form
host = 'localhost'
port = 8123

reactor.listenTCP(port, unoFactory())
print(f"Server started on host {host} port {port}")
print(f"Today we will allow {maxConnections} people to play UNO. Waiting for all to join...")
reactor.run()
