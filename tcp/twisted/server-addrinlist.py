#!/usr/bin/python3 

from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver


##TODO
#add comments to describe whats happening
#unify this to be JUST player logic.
class UnoPlayers(LineReceiver):
    def __init__(self, players, addr, maxCons):
        self.players = players #list of players
        self.addr = addr
        self.name = None
        self.state = "GETNAME"
        self.maxConnections = maxCons

    def connectionMade(self):
        printToLog(f"Player joined the lobby. Info: {self.addr}")
        printToLog(f"Num of current clients: {len(self.players.keys())+1}")
        printToLog(f"Waiting for more players....", '\n\n')
    
        self.players[self.addr] = self

        self.sendLine(b"Thanks for joining the game. Please choose an alias: ")

    def connectionLost(self, reason):
        printToLog(f"Player {self.name} left the lobby. Info: {self.addr}", '\n',"DC")
        if self.addr in self.players:
            del self.players[self.addr] 
        printToLog(self.players)

    def lineReceived(self, line): #change to switch case later
        if self.state == "GETNAME":
            self.handle_GETNAME(line)
        else:
            self.handle_AWAITING_START(line)

    def handle_GETNAME(self, name):
        self.name = name.decode()
        self.state = "AWAITING_START"
        self.sendLine(b"Thanks. Waiting for everyone to be ready....")
        self.sendLine(b"Options: r to change alias, q to quit.")
        printToLog(f"{self.name} is ready!")

        #iter through players here
        #game start condition:
        #all players are in state AWAITING_START and max players are achieved.
        
        if len(self.players) == self.maxConnections:
            for plyr, protocol in self.players.items():
                protocol.state = "BEGIN"
        
        #prints the status of every player connected & registered
        printToLog(f"List of plyrs: ")
        for plyr, protocol in self.players.items(): #Players is a list of TUPLES. name in bytes, protocol is where the meat dwells.
            printToLog(f"{protocol.name} {protocol.addr} | STATUS: {protocol.state}", '\n', f"PLAYER{list(self.players.keys()).index(protocol.addr)}")
        return
        printToLog(f"End List")

    def handle_AWAITING_START(self, line):
        if line.decode() == "r":
            self.state = "GETNAME"
            self.sendLine(b"\nNew alias?")
            printToLog(f"Heads up. {self.name} is changing their alias.")
        return
        #print whose in the lobby
        #continually update

class doNothing(UnoPlayers):
    pass

class unoFactory(Factory):
    def __init__(self, maxCons):
        # sets up array for every player to be stuck into
        self.players = {}
        self.maxConnections = maxCons
        self.currentCons = 0

    def buildProtocol(self, addr):
        if self.currentCons < self.maxConnections:
            self.currentCons += 1
            return UnoPlayers(self.players, addr, self.maxConnections)
        else:
            protocol = doNothing()
            protocol.factory = self
            return protocol

def printToLog(s: str, end = "\n", st = "LOG"):
    if end != "\n":
        print(f"{st}: {s}", end = end)
        return
    print(f"{st}: {s}", end = end)
    return


#https://stackoverflow.com/questions/30196186/how-to-limit-the-number-of-simultaneous-connections-in-twisted


#build mainloop later
#build exception handler later if the tcp connection fails to form
host = 'localhost'
port = 8123

maxConnections = 1 

reactor.listenTCP(port, unoFactory(maxConnections))
printToLog(f"Server started on host {host} port {port}")
printToLog(f"Today we will allow {maxConnections} people to play UNO. Waiting for all to join...")
reactor.run()
