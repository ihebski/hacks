l = []
n = []
for _ in range(3):
	l.append(int(input()))
n.append(l[0]+l[1]*l[2]) 
n.append(l[0]*(l[1]+l[2]))
n.append(l[0]*l[1]*l[2])
n.append((l[0]+l[1])*l[2])
n.append(l[0]+l[1]+l[2])
print max(n)