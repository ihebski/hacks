import sys 

def decrypt(k,cipher):
	plaintext = ''
	
	for each in cipher:
		p = (ord(each)-k) % 126
	
		if p < 32:
			p+=95
						
		plaintext += chr(p)
		
	if "flag" in plaintext or "FLAG" in plaintext or "FL4G" in plaintext:
		print "[Flag ] "+plaintext
		exit(0)
	else:
		print "key["+str(k)+"]  =>  "+plaintext	

def main(argv):
	cipher = "vuro"
		
	for i in range(1,25,1):
		decrypt(i,cipher)

if __name__ == "__main__":
	main(sys.argv[1:])
