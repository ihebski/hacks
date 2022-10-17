for _ in range(int(input())):
	s = raw_input().strip()
	c = 0
	for x in range(0,len(s)-1):
		if s[x] == s[x+1]:
			c +=1
	print c		

