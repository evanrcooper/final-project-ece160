# SENDING A CARD VIA ~THE INTERNET!~

The internet is magical.  
All this has is 2 files:  
<pre>
server.py:  used to FIRST get info on what card to send, and
            SECOND start a TCP socket and share the cards data to..

card_network.py:    A script which endlessly listens on localhost
            port 12345, until it gets a connection. It takes the
            data, unpacks, and draws the card.
</pre>
Fun!
