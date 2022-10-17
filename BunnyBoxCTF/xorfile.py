b = bytearray(open('secret.enc', 'rb').read())
l=[0x13,0x37]
for i in range(len(b)):
	b[i] ^= l[i%2]
open('b', 'wb').write(b)
