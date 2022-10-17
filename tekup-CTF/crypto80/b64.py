import base64
#flag = "flag{d41d8cd98f00b204e9800998ecf8427e}"

flag_morse ="..-. .-.. .- --. # -.. ....- .---- -.. ---.. -.-. -.. ----. ---.. ..-. ----- ----- -... ..--- ----- ....- . ----. ---.. ----- ----- ----. ----. ---.. . -.-. ..-. ---.. ....- ..--- --... . #" 

f = open("crypto80","w")
cc = flag_morse
for i in xrange(45):
	a = base64.b64encode(cc)
	cc = a
f.write(cc+"\n")
f.close()