import hashlib
import requests
import time
import binascii
from bs4 import BeautifulSoup

cookie={'PHPSESSID':'9fvoqsjb6c9unl6ju54odgd2d5'}
task ="56"

url = "https://ringzer0team.com/challenges/"+task

def hash512(data):
	return hashlib.sha512(data).hexdigest()

def submit_flag(data):
	r = requests.get("https://ringzer0team.com/challenges/"+task+"/"+data,cookies=cookie)
	return r.content


def decryptHash(data):
	a = requests.get("http://hashtoolkit.com/reverse-hash?hash="+data).content
	soup = BeautifulSoup(a,"lxml")
	badges = str(soup.find("span", {"title": "decrypted sha1 hash"}))
	return badges[badges.find(">")+1:badges.find("/span")-1]





def text(data):
	htmlContent = data
	begin = htmlContent.find("BEGIN")+30
	end = htmlContent.find("END")-20
	recv = htmlContent[begin:end]
	return recv

def main(data):
	recv = str(text(str(data)))
	print(recv)
	msg = submit_flag(str(decryptHash(recv))) 

	if "FLAG" in str(msg):
		msg = str(msg)
		print(msg[msg.find("FLAG"):msg.find("FLAG")+33])





if __name__ == '__main__':
	r1 = requests.get(url, cookies=cookie)
	print("[+] Connect ")
	main(r1.content)
	