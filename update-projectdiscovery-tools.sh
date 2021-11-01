#!/bin/bash
# Update projectdiscovery tools 
#projectdiscovery tools https://github.com/projectdiscovery
projectDiscovery=("httpx"  "nuclei"  "naabu"  "subfinder")
 
for tool in ${projectDiscovery[*]}; do
    curl -s https://api.github.com/repos/projectdiscovery/${tool}/releases/latest | grep "browser_download_url" | cut -d '"' -f 4 | grep "linux_amd64" | wget -qi - && unzip ${tool}* && sudo mv ${tool} /usr/bin/ && ${tool} -version
done
 
