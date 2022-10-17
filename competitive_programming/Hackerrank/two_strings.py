'''
Two Strings ,HAcker rank
'''
#!/bin/python

import sys

def check(s1,s2):
	s1 = list(set(s1))
	s2 = list(set(s2))
	test = "NO"
	i = 0
	while i< len(s1) and test is not "YES":
		if s1[i] in s2:
			test = "YES"
		else:
			i = i +1	
	return test		



q = int(raw_input().strip())
for a0 in xrange(q):
	s1 = raw_input().strip()
	s2 = raw_input().strip()
	print check(s1,s2)