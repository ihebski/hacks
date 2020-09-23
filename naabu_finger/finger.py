#!/usr/bin/env python3 
# -*- coding:utf-8 -*- 
'''
Fingerprint port services
Usage:
		cat targets | naabu | python3 finger.py  

Service list extract from: https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?&page=1 
by ihebski ( @ih3bski https://github.com/ihebski)
'''
import fileinput
import json

def finger(port):
	for row in data:
		if row["Port_Number"] == port:
			return f':{row["Service_Name"]} {row["Description"]}'
	return ""
	

with open('service-names-port-numbers.json') as f:
  data = json.load(f)

with fileinput.input() as f_input:
    for line in f_input:
    	print(f'{line.strip()}{finger(line.strip().split(":")[1])}')
