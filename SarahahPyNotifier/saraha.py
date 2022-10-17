#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Python Script to automatically get alerts notification on Desktop for Saraha.com website 
# You need cookies to run the script | script fetch for new msg every 1 min u can change it later
# Usage : python saraha.py 


import subprocess
import time
from bs4 import BeautifulSoup
import requests 
import os
import os.path



headers={
	"Cookie":"__YOUR_COOKIES_HERE__",
	"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:51.0) Gecko/20100101 Firefox/51.0",
	"content-type":"text"
}

fileName ="saraha.com"


# Parse the msg numbers from the server
def loginParser():
	r=requests.get("http://sarahah.com/Messages", headers=headers);
	#r = requests.get("http://127.0.0.1/saraha.php")
	c = r.content
	print "[+] parsing data"
	soup = BeautifulSoup(c,"lxml")
	msgNumber = soup.find_all("h5", {"class": "m-y-0 text-inherit"})[0].string
	return msgNumber

#write the first file with a default msg number 0
def WriteDb(data):
	try:
		with open(fileName, "w") as outfile:
			outfile.write(data)
	except IOError:
		print 'oops! can not create db !'

#Check if the file exists
def checkFile():
	if os.path.isfile(fileName) and os.access(fileName, os.R_OK):
		return 1
	else:
		return 0


# Alert user with new recieved msg
def sendMessage(message):
    subprocess.Popen(['notify-send', message])
    return

# Compare the parsed value with the old one and push a notification
def getNotification(oldMsg,NewMsg):
	s1 = int(oldMsg)
	s2 = int(NewMsg)
	if s2 > s1:
		sendMessage("Saraha.com! You have New msg !")
		WriteDb(NewMsg)

# Read the lastest MSG number stored from the server
def ReadMyDb():
	with open(fileName, "r") as f:
		for line in f:
			return str(line)		

# Do all the dirty things lollz

def main():
	if checkFile() == 0:
		WriteDb("0")
	else:
		oldMsg = ReadMyDb()
		NewMsg = loginParser()
		getNotification(oldMsg,NewMsg)	
	


# Run the application
if __name__ == '__main__':
	print "[+] Script starts"
	while 1:
		main()
		# Set the time to 2 min if you went less remove the comment tag and comment the last line
		#time.sleep(time.localtime(time.time())[5]) 
		time.sleep(60) # Sleep for 1 min


