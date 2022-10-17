


def count_sort(arr,maxval):
	m = maxval +1
	count = [0]*m
	for a in arr:
		count[a] +=1
	return count	



n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
for x in count_sort(a,max(a)):
	print x,

