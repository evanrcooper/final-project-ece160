#!/bin/bash

#set up pipes:
mkfifo $PWD/pipe1
mkfifo $PWD/pipe2

gcc $PWD/cWriter.c &&
$PWD/a.out &
$PWD/pyReader.py &&

#cleaning
rm $PWD/pipe1
rm $PWD/pipe2
rm $PWD/a.out
exit
