# bash pulseSecureVersion.sh 127.0.0.1

IP=$1
# Pulse secure version <= R8
curl -k https://$IP/dana-na/nc/nc_gina_ver.txt | grep '<PARAM NAME="ProductVersion" VALUE="'

# Pulse secure version > R8 (R9 >>)
curl -k https://$IP/dana-cached/hc/HostCheckerInstaller.osx -o version && strings version | grep '<string>'
