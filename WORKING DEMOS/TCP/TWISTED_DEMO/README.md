This is the Twisted logic, written by James  
Instructions:  
<pre>
1. start server.py on localhost
2. on the same machine, start an instance of client.py
3. on client.py, connect with host "localhost"
4. enter a name
5. rinse and repeat for player 2.
6. game starts!
</pre>

The big idea with this was that each client which connects works off as a "state"  
The state just tells the server how to deal with a clients input, and tells a client whether or not they can send an input.  
To deal with race conditions and whatnot, only one client is supposed to be able to speak at a time.  
The server assigns each client a state, such as "GETNAME", which ideally asks a client to speak, and then the User at  
that client will speak, via string input or whatever.  
Its just a method of bookkeeping.  
