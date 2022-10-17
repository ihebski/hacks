s = raw_input().strip()
c = 0
while c < len(s) -1 :
	if s[c] == s[c+1]:
		s = s[:c]+s[c+2:]
		c = 0
	else:
		c +=1

print s if s is not '' else "Empty String" 	
