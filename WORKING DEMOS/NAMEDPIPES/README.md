# NAMED PIPES WITH MKFIFO
<pre>
I opted to try working with named pipes instead of the convoluted
"poke" system, and it seems to be working fairly decently

named pipes are just "files" which can be written to and read from, but when one
is written to, the process goes to sleep waiting for it to be accessed.
This fits nicely with my pre-conceived poke system, and hopefully
should be an efficient solution

attached is a demo. named pipes are made, programs ran, pipes used,
then pipes deleted after success. only tested in fedora linux.
</pre>
