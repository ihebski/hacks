import base64

f=open("crypto80", "a+")
flag = f.read()
for x in xrange(45):
	d = base64.b64decode(flag)
	flag = d
print flag