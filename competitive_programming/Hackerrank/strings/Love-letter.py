
for _ in range(int(input())):
	s = raw_input().strip()
	n = len(s)/2
	if len(s) % 2 ==0 :
		l,r = s[:n],s[n:]
	else:
		l,r = s[:n],s[n+1:]
	a = map(ord,l)[::-1]
	b = map(ord,r)
	c = 0
	for i in range(len(a)):
		c+=abs(a[i]-b[i])	
	print c	