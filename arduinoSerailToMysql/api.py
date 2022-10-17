'''
Auto connect to the serial port of Arduino board ,parse DATA and sent it to API hosted to server
Arduino ->Serial->api.py->API>DB
Written by @IhebBenSalem
'''
import serial, sys, string
import time, datetime, httplib
import serial.tools.list_ports
import sys
import atexit
import platform
import requests
from random import randint
import time
#------------------------------------------------------------------------#
#variable :set the default value of variable
#------------------------------------------------------------------------#
host = "localhost"
path = "API"
locations=['/dev/ttyUSB0','/dev/ttyUSB1','/dev/ttyUSB2','/dev/ttyUSB3',
'/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM3','/dev/ttyS3']  
 #-----------------------------------------------------------------------# 
for device in locations:  
	try:  
		print "Trying...",device
		serial_data = serial.Serial(device, 9600) 
		break
	except:  
		print "Failed to connect on",device   

try:  
    
 while 1:

    # Read in line of readings from emontx serial
    linestr = serial_data.readline()

    # Remove the new line at the end
    linestr = linestr.rstrip()
    # print "DATA RX:"+linestr
    print linestr

    #Send to API
    r = requests.get("http://"+host+"/"+path+"/api.php?code="+str(linestr))
    print r.text
    time.sleep(1)


except:  
    print "Failed to send!" 

