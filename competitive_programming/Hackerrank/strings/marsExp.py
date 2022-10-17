a = raw_input().strip()
b = [a[i:i + 3] for i in range(0, len(a), 3)]
c = 0
for x in b:
	if x[0] is not "S":
		c +=1
	if x[1] is not "O":
		c += 1
	if x[2] is not "S":
		c += 1
print c					
