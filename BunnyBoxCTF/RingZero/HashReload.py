import hashlib
import requests
import time
import binascii
cookie={'PHPSESSID':'9fvoqsjb6c9unl6ju54odgd2d5'}
task ="14"

url = "https://ringzer0team.com/challenges/"+task

def hash512(data):
	return hashlib.sha512(data).hexdigest()

def decode_binary_string(s):
	return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))


def submit_flag(data):
	r = requests.get("https://ringzer0team.com/challenges/"+task+"/"+data,cookies=cookie)
	return r.content


def text(data):
	htmlContent = data
	begin = htmlContent.find("BEGIN")+33
	end = htmlContent.find("END")-20
	recv = htmlContent[begin:end]
	return recv

def main(data):
	recv = text(str(data))
	print("recv : ",recv,decode_binary_string(recv))
	rec = decode_binary_string(recv)
	getHash = hash512(rec.encode())
	msg = submit_flag(str(getHash)) 
	if "FLAG" in str(msg):
		msg = str(msg)
		print(msg[msg.find("FLAG"):msg.find("FLAG")+33])






if __name__ == '__main__':
	r1 = requests.get(url, cookies=cookie)
	print("[+] Connect ")
	main(r1.content)




	#print(main(a))
