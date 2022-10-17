from collections import Counter

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

s = Counter(a)

for k,v in s.iteritems():
	if v == 1:
		print k