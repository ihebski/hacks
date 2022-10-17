

try: 
	import re
	import requests
	from bs4 import BeautifulSoup 
	import sys
	import os
	from beautifultable import BeautifulTable
except Exception as err:
	print "[!] "+str(err)
	sys.exit(0)

baseUrl = "http://www.routerpasswords.com"




def GetRouterPassword(routerName):
	r = requests.post(baseUrl, data = {'findpass':'1','router':routerName,'findpassword':'Find+Password'})
	soup = BeautifulSoup(r.text,"lxml")
	"""
	for option in soup.find_all('option'):
		print "list"
	"""
	# Parse table specification
	table = soup.find("table")
	headings = [th.get_text() for th in table.find("tr").find_all("th")]
	datasets = []
	mylist = []
	for row in table.find_all("tr")[1:]:
	    dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
	    datasets.append(dataset)
	
	for dataset in datasets:
	    for field in dataset:
	    	mylist.append(field[1])
	# Group forms for the table rows
	tmp = []
	s = []
	i = 0
	for x in mylist:
		i +=1
		tmp.append(x)
		if i == 5:
			tmp = []
			i = 0
			s.append(tmp)	
	# Draw the table rows and columns		
	table = BeautifulTable()
	table.column_headers = ["Manufacturer", "Model", "Protocol","Username","Password"]
	for y in xrange(0,len(s)):
		if len(s[y]) > 0:
			table.append_row(s[y])
	print table



def GetRouterList():
	r = requests.post(baseUrl, data = {'findpass':'1','router':"CISCO",'findpassword':'Find+Password'})
	soup = BeautifulSoup(r.text,"lxml")
	for option in soup.find_all('option'):
		print option["value"]
	

def usage():
	print "python routerdb.py RouterName"	

if __name__ == '__main__':
	#GetRouterList()
	GetRouterPassword("CISCO")

