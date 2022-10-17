import hashlib
import requests
import time
cookie={'PHPSESSID':'9fvoqsjb6c9unl6ju54odgd2d5'}
task ="32"

url = "https://ringzer0team.com/challenges/"+task

def hash512(data):
	return hashlib.sha512(data).hexdigest()



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
	print("recv : ",recv)
	m = recv.split(" ")
	s = int(m[0]) + int(m[2],16) - int(m[4],2)
	print(s) 
	#getHash = hash512(recv.encode())
	msg = submit_flag(str(s)) 
	if "FLAG" in str(msg):
		msg = str(msg)
		print(msg[msg.find("FLAG"):msg.find("FLAG")+35])






if __name__ == '__main__':
	r1 = requests.get(url, cookies=cookie)
	print("[+] Connect ")
	main(r1.content)




	#print(main(a))
