#!/bin/bash
# Update google chrome to the latest version (Linux)

chrome_installed_version=$(google-chrome --version | awk '{print $3}')
chrome_current_version=$(curl https://omahaproxy.appspot.com/linux --silent)

if [ "$chrome_installed_version" = "$chrome_current_version" ]; then
    echo "[!] We are running the latest version of Google chrome"
else
    echo "[+] Installing the new version of Google Chrome -> [ $chrome_current_version ]"
    wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -P /tmp && sudo dpkg -i /tmp/google-chrome-stable_current_amd64.deb
fi
