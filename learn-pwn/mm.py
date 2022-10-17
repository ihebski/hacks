import binascii
from more_itertools import sliced
import sys
# reverse memory address from 0x080483d0 to \xd0\x83\x04\x08
print repr(binascii.unhexlify(''.join(list(sliced(str(sys.argv[1]).replace("0x",""),2))[::-1])))
