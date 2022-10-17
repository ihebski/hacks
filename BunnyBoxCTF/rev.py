from pwn import *
import hashlib
letter_to_morse = {
    "a" : ".-",     "b" : "-...",     "c" : "-.-.",
    "d" : "-..",    "e" : ".",        "f" : "..-.",
    "g" : "--.",    "h" : "....",     "i" : "..",
    "j" : ".---",   "k" : "-.-",      "l" : ".-..",
    "m" : "--",     "n" : "-.",       "o" : "---",
    "p" : ".--.",   "q" : "--.-",     "r" : ".-.",
    "s" : "...",    "t" : "-",        "u" : "..-",
    "v" : "...-",   "w" : ".--",      "x" : "-..-",
    "y" : "-.--",   "z" : "--..",     " " : "/",
    '0': '-----',   '1': '.----',     '2': '..---',
    '3': '...--',   '4': '....-',     '5': '.....',
    '6': '-....',   '7': '--...',     '8': '---..',
    '9': '----.' 
}

morse_to_letter = {morse: letter for letter, morse in letter_to_morse.items()}

def decode_morse(morse_code):
    return ''.join(morse_to_letter[code] for code in morse_code.split())
def md5(st):
	print hashlib.md5(st).hexdigest()
	return hashlib.md5(st).hexdigest()
	 
def sha256(st):
	print hashlib.sha256(st).hexdigest()
	return hashlib.sha256(st).hexdigest()

def sha1(st):
	print hashlib.sha1(st).hexdigest()
	return hashlib.sha1(st).hexdigest()


s = remote('217.182.84.50',8080)

a= s.recv(1024)
a= s.recv(1024)

print a

c= decode_morse(a).decode('hex')
print c
tab= c.split("(")
hash=tab[3][:-3]
print tab[0]
print tab[1]
print tab[2]

print hash
if(tab[2]=="md5"):
	hash=md5(hash)
elif(tab[2]=="sha256"):
	hash=sha256(hash)
elif(tab[2]=='sha1'):
	hash=sha1(hash)

if(tab[1]=="md5"):
	hash=md5(hash)
elif(tab[1]=="sha256"):
	hash=sha256(hash)
elif(tab[1]=='sha1'):
	hash=sha1(hash)

tab[0]=tab[0][9:]

if(tab[0]=="md5"):
	hash=md5(hash)
elif(tab[0]=="sha256"):
	hash=sha256(hash)
elif(tab[0]=='sha1'):
	hash=sha1(hash)
s.send(hash)
print hash
print s.recv(1024)



	










