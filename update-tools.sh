# Update httpx
curl -s https://api.github.com/repos/projectdiscovery/httpx/releases/latest | grep "browser_download_url" | cut -d '"' -f 4 | grep "linux_amd64" | wget -qi - && unzip httpx* && sudo mv httpx /usr/bin/ && httpx -version
