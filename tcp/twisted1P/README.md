<pre>
c_readin - python writes to this file, c reads it.
py_readin - c writes to this file, py reads it.

what do they read? messagepack data, encoded to be whatever they need. 
	c needs to know whos playing. sure, python writes to c_readin with a messagepack on how many players there is
	
	python needs a players deck. sure thing, c writes to py_readin w/ the card array encoded.
	c needs a choice. sure thing, python writes a specific card type to c_readin

How do they know when they're listening?
3 way handshake
c writes 1 to py_readin, py writes 1 to c_readin, c writes 0 to py_readin
</pre>