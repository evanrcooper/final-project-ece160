#!/usr/bin/python3 
"""
Helper which sets up Uno game for players to connect.
Manages players and active sockets.
Facilitates gameplay flow between C and Python.

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠴⠤⠤⠴⠄⡄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⠄⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠁⠃⠆⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡜⠁⠀⠀⠀⢠⡄⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠑⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢈⠁⠀⠀⠠⣿⠿⡟⣀⡹⠆⡿⣃⣰⣆⣤⣀⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣼⠀⠀⢀⣀⣀⣀⣀⡈⠁⠙⠁⠘⠃⠡⠽⡵⢚⠱⠂⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⢐⣢⣤⣵⡄⢀⠀⢀⢈⣉⠉⠉⠒⠤⠀⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⡇⠀⠀⠀⠀⠀⠉⠉⠁⠁⠈⠀⠸⢖⣿⣿⣷⠀⠀⢰⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⠃⠀⡄⠀⠈⠉⠀⠀⠀⢴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀uno⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢈⣇⠀⠀⠀⠀⠀⠀⠀⢰⠉⠀⠀⠱⠀⠀⠀⠀⠀⢠⡄⠀⠀⠀⠀⠀⣀⠔⠒⢒⡩⠃⠀tcp⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣴⣿⣤⢀⠀⠀⠀⠀⠀⠈⠓⠒⠢⠔⠀⠀⠀⠀⠀⣶⠤⠄⠒⠒⠉⠁⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡄⠤⠒⠈⠈⣿⣿⣽⣦⠀⢀⢀⠰⢰⣀⣲⣿⡐⣤⠀⠀⢠⡾⠃⠀⠀⠀⠀⠀⠀⠀⣀⡄⣠⣵⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⠏⢿⣿⡁⢐⠶⠈⣰⣿⣿⣿⣿⣷⢈⣣⢰⡞⠀⠀⠀⠀⠀⠀⢀⡴⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢿⣿⣍⠀⠀⠸⣿⣿⣿⣿⠃⢈⣿⡎⠁⠀⠀⠀⠀⣠⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢙⣿⣆⠀⠀⠈⠛⠛⢋⢰⡼⠁⠁⠀⠀⠀⢀⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⣷⣧⣷⣤⡶⠎⠛⠁⠀⠀⠀⢀⡤⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠁⠀⠀⠀⠀⠀⠠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""


from twisted.internet import reactor
from twisted.internet.protocol import Factory, Protocol
from twisted.protocols.basic import LineReceiver

import os
import time

WAITSIG = b"__WAIT__"
QUERSIG = b"__QUERY__"
SURESIG = b"__SURE__"

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
        if self.state == "AWAITING_CONF":
            self.handle_AWAITING_CONF(line)
        if self.state == "GETNAME":
            self.handle_GETNAME(line)
        elif self.state == "BEGIN":
            self.handle_BEGIN(line)
        else:
            self.handle_AWAITING_START(line)

    """
    Client server relationship can be seen in more depth in client.py
    There are ### states which the server can exist as:
    GETNAME - QUERIES the client (Player) for their name.
    WAITING - Waits for every Player to connect
    BEGIN - Queries C for each card set. dishes out each 
        card set. Each Player is given their UNIQUE set

    Output is in primary-secondary format
        Primary output: Game state and specific questions,
            like "card to play?"
        Secondary output: Game state. Dished out via a loop
            which addresses every Player except the one
            currently being queried.
    """

    def handle_GETNAME(self, name):
        self.name = name.decode()
        self.name = self.name.strip()
        if self.name == "":
            self.sendLine(b"Invalid name, try again.")
            return
        self.state = "AWAITING_START"
        self.sendLine(b"Thanks. Hang tight while everyone joins.")
        self.sendLine(b"^C to quit. You cannot abandon when the game starts.")

        printToLog(f"{self.name} is ready!")

        #iter through players here
        #game start condition:
        #all players are in state AWAITING_START and max players are achieved.
        
        if len(self.players) == self.maxConnections:
            for plyr, protocol in self.players.items():
                protocol.state = "BEGIN"
                printToLog(f"sent notice to {protocol.name}")

            #Waits for player to accept their fate
            printToLog(f"Game starts with {self.name}")
            self.sendLine(QUERSIG)
            self.state = "AWAITING_CONF"

        #prints the status of every player connected & registered
        printToLog(f"List of plyrs: ")
        for plyr, protocol in self.players.items(): #Players is a list of TUPLES. name in bytes, protocol is where the meat dwells.
            printToLog(f"{protocol.name} {protocol.addr} | STATUS: {protocol.state}", '\n', f"PLAYER{list(self.players.keys()).index(protocol.addr)}")
        printToLog(f"End List")
        return 

    def handle_AWAITING_START(self, line):
        """
        if line.decode() == "r":
            self.state = "GETNAME"
            self.sendLine(b"New alias?")
            printToLog(f"Heads up. {self.name} is changing their alias.")
        else:
            self.sendLine(b"Invalid Input.")
        return
        """
        #print whose in the lobby
        #continually update

    def handle_AWAITING_CONF(self, line):
        printToLog(line)
        if SURESIG.decode() in line.decode():
            printToLog("SURESIG Received... gaem is a go")
            self.state = "BEGIN" #TEMP!!!!!!!!!
            return
        printToLog("Received the wrong information. IMPLEMENT REDO", "\n", "Failure")
        return

    def handle_BEGIN(self, line):
        printToLog("All players are ready to play")
        for plyr, protocol in self.players.items():
            protocol.sendLine(b"All players have arrived. Now we begin.")
        return

class doNothing(Protocol):
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
    #FIX ME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def oneConnectionDisconnected(self):
        self.currentCons -= 1
        if self.currentCons > 0 and not (self.players[0].state == "GETNAME" or self.players[0].state == "AWAITING_START"):
            for plyr, protocol in self.players.items():
                protocol.sendLine("Player Disconnected! Game will now end.")
                reactor.stop()

def printToLog(s: str, end = "\n", st = "LOG"):
    #set up string to write, file to write to (latest_log)
    toAppend = ""

    #set up log line formatting
    #kind of nonsensical, why do i if here? wtf
    if end != "\n":
        toAppend += f"{st}: {s}{end}"
        print(toAppend)
        #print(f"{st}: {s}", end = end)
        return
    toAppend += f"{st}: {s}"
    print(toAppend)
    #print(f"{st}: {s}")
    
    #write to file
    return


#https://stackoverflow.com/questions/30196186/how-to-limit-the-number-of-simultaneous-connections-in-twisted


#build mainloop later
#build exception handler later if the tcp connection fails to form
host = 'localhost'
portForLocalC = 8246
portForClients = 8123

maxConnections = 2 

#Now that the C and Pyth have a pipe, we can start accepting internet connections.
reactor.listenTCP(portForClients, unoFactory(maxConnections))
printToLog(f"Server started on host {host} port {portForClients}")
printToLog(f"Today we will allow {maxConnections} people to play UNO. Waiting for all to join...")
reactor.run()
