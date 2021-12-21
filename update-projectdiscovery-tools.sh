#!/bin/bash
# Update projectdiscovery tools by @ihebski

#projectdiscovery tools https://github.com/projectdiscovery
projectDiscovery=("httpx"  "nuclei"  "naabu"  "subfinder")

for tool in ${projectDiscovery[*]}; do
    # Get latest tools release
    url=$(curl -s https://api.github.com/repos/projectdiscovery/${tool}/releases/latest | grep "browser_download_url" | cut -d '"' -f 4 | grep "linux_amd64")
    # Extract versions
    new_version=$(basename $url | grep -Eo '[0-9]+([.][0-9]+)?+([.][0-9]+)')
    installed_version=$(${tool} -version &> /tmp/v ; grep "INF" /tmp/v | grep -Eo '[0-9]+([.][0-9]+)?+([.][0-9]+)' )

    if [ "$installed_version" = "$new_version" ]; then
        printf "\nWe are running the latest version of ${tool} \U1F44D\n"
    else
        printf "\n[+] Installing the new version of ${tool} -> [ $new_version ] \U1F50E\n"
        # Download and install the new version of tools
        wget --show-progress -q $url -P /tmp && unzip /tmp/${tool}* -d /tmp && sudo mv /tmp/${tool} /usr/bin/ && rm /tmp/${tool}* /tmp/v
    fi
done
