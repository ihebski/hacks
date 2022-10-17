import hashlib 
import base64
import binascii
import optparse
from colorama import Fore, Back, Style 

# Colors
YL = '\033[93m'
LIGHTRED = '\033[91m'

def Usage():
	print "python hashLab.py -e md5 -w text\n"
	print "python hashLab.py -d bin -w 11001110\n"
	print "python hashLab.py -r FLAG \n"


def text2bin(text, encoding='utf-8', errors='surrogatepass'):
	# IN  : Text
	# OUT : BIN
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def bin2text(bits, encoding='utf-8', errors='surrogatepass'):
    '''
	IN  : BIN
	OUT : TEXT 
    '''
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))


# ENCODE hash
def md5(hash):
	return hashlib.md5(hash).hexdigest()

def sha1(hash):
	return hashlib.sha1(hash).hexdigest()

def sha224(hash):
	return hashlib.sha224(hash).hexdigest()

def sha256(hash):
	return hashlib.sha256(hash).hexdigest()

def sha384(hash):
	return hashlib.sha384(hash).hexdigest()

def sha512(hash):
	return hashlib.sha512(hash).hexdigest()

def base64_encode(text):
	return base64.b64encode(text)

def base64_decode(text):
	return base64.b64decode(text)


def revText(text):
	'''
	Resverse TEXT 
	IN  : abc
	OUT : cba 
	'''
	return text[::-1]


def hex2Text(data):
	'''
	IN : Hex
	OUT: Ascci-Text
	'''
	return data.decode("hex")

def text2hex(s):
	'''
	IN  : Text
	OUT : Hex 
	'''
	return "".join("{0:x}".format(ord(c)) for c in s)


# Custom print 
def prints(opertaion,codes,value):
	print LIGHTRED+"["+opertaion+"]"+Fore.RESET+Fore.WHITE+"["+codes+"] "+Fore.RESET+ YL+value

def CesarBruteForce(k,cipher):
	'''
	Cesar BruteForce
	'''

	plaintext = ''
	
	for each in cipher:
		p = (ord(each)-k) % 126
	
		if p < 32:
			p+=95
						
		plaintext += chr(p)
		print plaintext
	if "flag" in plaintext or "FLAG" in plaintext or "FL4G" in plaintext:
		print LIGHTRED+"[Key="+str(k)+" FLAG] "+ Fore.RESET+YL+plaintext
		#exit(0)
	else:
		print "key["+str(k)+"]  =>  "+plaintext+"\n ============================"	


def main():
	# Parse options
	pars = optparse.OptionParser(description="HashLab")
	pars.add_option('-e', '--encode',action="store", dest="encode", type="string", help=" Encode hash md5,sha1,sha224,sha256,sha384,sha512,base64,bin,hex",default=None)
	pars.add_option('-d', '--decode',action="store", dest="dec", type="string", help=" decode base64 ,bin ,HEX, cesar",default=None)
	pars.add_option('-w', '--word',action="store", dest="word", type="string", help=" word to encode/decode",default=None)
	pars.add_option('-r', '--reverse',action="store", dest="reverse", type="string", help=" reverse text",default=None)
	opts, args = pars.parse_args()	
	# ENcode Section
	if opts.encode:
		if opts.encode not in ["md5","sha1","sha224","sha256","sha384","sha512","base64","bin","hex"]:
			print "[!] Not supported yet !"
		if opts.encode and opts.word :
			if opts.encode == "md5" :
				prints("Encode","md5",md5(opts.word))
			if opts.encode == "sha1":
				prints("Encode" ,"sha1",sha1(opts.word))
			if opts.encode == "sha224":
				prints("Encode","sha224",sha224(opts.word))
			if opts.encode =="sha256":
				prints("Encode","sha256",sha256(opts.word))
			if opts.encode == "sha384":
				prints("Encode","sha384",sha384(opts.word))
			if opts.encode == "sha512":
				prints("Encode","sha512",sha512(opts.word))
			if opts.encode == "base64":
				prints("Encode","base64",base64_encode(opts.word))
			if opts.encode == "bin":
				print opts.word
				prints("Encode","bin",text2bin(opts.word))	
			if opts.encode == "hex":
				prints("Encode","Hex",text2hex(opts.word))

	# Decode Secion			
	if opts.dec:
			if opts.dec not in ["bin","hex","base64","cesar"]:
				print "[!] Not supported yet !"
			if opts.dec and opts.word :
				if opts.dec == "bin" :
					prints("DEcode","bin", bin2text(opts.word))
				if opts.dec == "base64":
					prints("DEcode","Base64",base64_decode(opts.word))	
				if opts.dec == "hex":
					prints("DEcode","Hex",hex2Text(opts.word))	
				if opts.dec == "cesar":
					for k in range(1,26,1):
						CesarBruteForce(k,opts.word)		
	# Reverse text				
	if opts.reverse:
		prints("Reverse","TXT",revText(opts.reverse))				



if __name__ == '__main__':
	main()
