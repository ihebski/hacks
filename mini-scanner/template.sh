#!/bin/bash
# Script template
# 
# Usage :
# $ echo "host1 host2 host3" | ./scanner
# $ cat myservers | ./scanner
#
servers="$(cat)"

for servers in $servers; do
	# command test here
	echo $servers
done
