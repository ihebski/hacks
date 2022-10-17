#!/bin/bash

TARGET=$1
RECON_PATH=$2
SUB_PATH="$RECON_PATH/$TARGET"

# create subdomain directory
echo -e "[+] create directory"
mkdir -p $SUB_PATH/$TARGET

enumSubs(){
    echo -e "${GREEN}\n--==[ Enumerating subdomains ]==--${RESET}"
    
    echo -e "findomain-linux"
    findomain_virustotal_token="__TOKEN_HERE__"
    findomain_spyse_token="__TOKEN_HERE__"
    findomain_securitytrails_token="__TOKEN_HERE__"

    findomain-linux -o -t $TARGET -r
    mv $TARGET.txt $SUB_PATH/findomain_linux.txt

    echo -e "Amass"
    amass enum -passive -d $TARGET -o $SUB_PATH/amass.txt

    echo -e "Subfinder"
    subfinder -d $TARGET -t 50 -nW --silent -o $SUB_PATH/subfinder.txt
    
    echo -e "Sublister"
    python ~/tools/Sublist3r/sublist3r.py -d $TARGET -o $SUB_PATH/sublister.txt


    echo -e "Assetfinder"
    assetfinder -subs-only $TARGET > $SUB_PATH/assetfinder.txt
    
    echo -e "Certspotter"
    curl -s https://certspotter.com/api/v0/certs\?domain\=$TARGET | jq '.[].dns_names[]' | sed 's/\"//g' | sed 's/\*\.//g' | sort -u | grep $TARGET >> $SUB_PATH/certspotter.txt
    
    echo -e "Crtsh"
    crtsh -q %.$TARGET -o | tee -a $SUB_PATH/crtsh.txt

    echo -e "${RED}\n[+] Combining subdomains...${RESET}"
    cat $SUB_PATH/*.txt | sort | awk '{print tolower($0)}' | uniq > $SUB_PATH/final-subdomains.txt
    echo -e "${BLUE}[*] Check the list of subdomains at $SUB_PATH/final-subdomains.txt${RESET}"

}

waybackrecon () {
    echo -e "[+] Waybackurls"
    cat $SUB_PATH/final-subdomains.txt | waybackurls > $SUB_PATH/waybackurls.txt
}

bruteForce()
{

    echo -e "----- Brute force massdns ------ "
    massdns -r ~/tools/Sublist3r/subbrute/resolvers.txt -o S $SUB_PATH/final-subdomains.txt | grep -e ' A ' |  cut -d 'A' -f 1 | rev | cut -d "." -f1 --complement | rev | sort | uniq > $SUB_PATH/elcapo-massdns.txt

    echo -e "-------- DNS scan ---------"
    python ~/tools/dnscan/dnscan.py -d $TARGET -t 30 -w ~/tools/Sublist3r/subbrute/names.txt -o $SUB_PATH/elcapo-bruteForce-final.txt

    echo -e "amass bruteforce"
    amass enum -brute -w /opt/wordlist/commonspeak2-wordlists/subdomains/subdomains.txt -df $SUB_PATH/elcapo-massdns.txt -o $SUB_PATH/elcapo-amass-bruteForce.txt


}

enumSubs
waybackrecon
bruteForce
