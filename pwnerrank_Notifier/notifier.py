#!/usr/bin/python
# ex: python notifier.py 
# if new updates appairs a notification bar shown with the category name and the number of new tasks
import os
import re
#PLEASE INCLUDE YOUR COOKIES TO RUN THE SCRIPT
cmdCurl='curl --cookie "_YOURCOOKIES_HERE_" http://www.pwnerrank.com/categories/ | grep "<small>" >>pwnerrank.com'

task_list=['binary-exploitation', 'cryptography', 'computer-forensics', 'misc','programming','crack','steganography','web'];

def fetch_url():
	os.system(cmdCurl)
	os.system("clear")

def test():
	f = open("notifier.db","w")
	with open("pwnerrank.com", "r") as ins:
		array = []
		for line in ins:
			task_number=re.findall(r'\d+', line)
			task_name=line[25:28]
			save_file=task_name+" "+task_number[1]
			f.write(save_file+"\n")


def getNotification():
	array_new = []
	retarray=[]
	with open("notifier.db", "r") as f:
		for line in f:
			array_new.append(line[4])

	array_old = []
	with open("old.db", "r") as f:
		for line in f:
			array_old.append(line[4])
	for i in range(0,8):
		a=int(array_old[i])
		b=int(array_new[i])
		if (b>a):
			mych=str(i)+":"+str(b-a)
			retarray.append(mych)
	return retarray

def print_notification(network):
	if (len(network)==0):
		print "------------ NO UPDATES ----------------"
	for x in xrange(0,len(network)):
		t=network[x]
		tsk_name=int(t[0])
		added_task=int(t[2])
		print task_list[tsk_name],": +",added_task
		to_notify_system="notify-send "+str(task_list[tsk_name])+": +"+str(added_task)
		os.system(to_notify_system)

def clean_my_host():
	os.system("rm old.db")
	os.system("rm pwnerrank.com")
	os.system("mv notifier.db old.db")


def main():
	fetch_url()
	print "[+] Fetch url tasks"
	test()
	nt=getNotification()
	print_notification(nt)
	clean_my_host()

    
if __name__ == "__main__":
    main()
