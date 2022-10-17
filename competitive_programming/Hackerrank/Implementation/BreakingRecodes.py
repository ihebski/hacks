n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

low = arr[0]
Higher = arr[0]
count_Lower = 0
count_Higher = 0

for i in xrange(1,n):
	if arr[i] > Higher:
		Higher = arr[i]
		count_Higher +=1
	if  arr[i] < low:
		low = arr[i]
		count_Lower +=1
print count_Higher ,count_Lower		
