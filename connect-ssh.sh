#!/usr/bin/expect -f
set timeout 10
spawn ssh -o StrictHostKeyChecking=no root@192.168.1.3
expect "*?assword:*"
send -- "Password\r"
sleep 2
send -- "\r"
sleep 2
send -- "uptime \r"
sleep 2
send -- "exit\r"
expect eof
