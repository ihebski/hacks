import requests
import json
from terminaltables import AsciiTable



# Return token to be used as session
def getToken(username,password):
	return requests.post('http://127.0.0.1:8443/v1/session', data = {'username':username,"password":password}).text

# return all the reports available in the platefrom
def reportsList(ValidSession):
	r = requests.post('http://127.0.0.1:8443/v1/reports', data = {'session':ValidSession})
	j = r.json()
	l = []
	table_data = [["report_name","report_id"]]
	for item in j:
		l = [item['report_name'], item['id']]
		table_data.append(l)
	table = AsciiTable(table_data)
	#pirnt table
	print table.table


# Input :float score return severity Critical ,High ,meduim ,low
def severity(score):

	if score >= 9 :
		s = "Critical"
	elif score >=7 and score <9 :
		s = "High"
	elif score >=4 and score <7 :
		s = "Medium"
	elif score > 0 and score <4 :
		s = "Low"
	else:
		s = "0"
	return str(s)			
		
# Parse all the findings and create CVS file format
def findings_to_csv(mysession,reportId):
	f = open("myreport.csv","w")
	f.write("reference|Findings|Description|Severity|cvss3|Assests"+"\n")
	i = 0
	j = requests.post('http://127.0.0.1:8443/v1/findings', data = {'session':mysession,'report_id':reportId}).json()
	print type(j)
	for i,finding in enumerate(j):
		print finding["title"]
		print finding["overview"].encode("utf-8")
'''
	for item in j:
		i+=1
		ref = str("Int"+str(i))
		title = item["title"]
		sev = severity(item["cvss_environmental"])
		cvss3 = str(item["cvss_environmental"])
		Asessts = item["affected_hosts"].replace('<paragraph>','').replace('</paragraph>','')
		description = item["overview"].replace('<paragraph>','').replace('</paragraph>','') 
		f.write(ref+"|"+title+"|"+description+"|"+sev+"|"+cvss3+"|"+Asessts+"\n")
	f.close()	
'''

if __name__ == '__main__':
	# Username/password to create session
	#username = raw_input("username: ")
	#pwd = raw_input("password: ")
	username = ""
	pwd = ""
	mysession = getToken(username,pwd)
	reportsList(mysession)
	# Select report id
	rep_id = raw_input("Report id: ")
	# Generate report
	findings_to_csv(mysession,rep_id)
	print "Done [#################################] 100%"
