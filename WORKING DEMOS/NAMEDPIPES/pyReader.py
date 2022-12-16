#!/usr/bin/python3
#reads named pipe
#stops on delimiter

def readFromBuffer(file):
    inputPipe = open(file, "r")
    buffer = inputPipe.read()
    inputPipe.close()

    return buffer

def writeToBuffer(buffer, file):
    outputPipe = open(file, "w")
    outputPipe.write(buffer)
    outputPipe.close()

    return

buffer = readFromBuffer("pipe2")
print(buffer)
writeToBuffer("Ok. Sure. Whatever.", "pipe1")
