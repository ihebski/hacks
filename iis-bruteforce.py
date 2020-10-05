# IIS short filename bruteforce/eneumeration 
# @ihebski
import difflib

wordlist = open("./common.txt").read().splitlines()
iis_short = ["RESOUR","WEBCON","USERTAD","CUSTOM","USERLI","CONTEN","DOWNLO","API.ASP"]

for path in iis_short:
	print(f'[+] Possible full path name for {path}: \n{difflib.get_close_matches(path.lower(), wordlist)}\n')
