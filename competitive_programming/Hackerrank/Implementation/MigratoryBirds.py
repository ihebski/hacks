n = int(raw_input().strip())
arr =  map(int, raw_input().strip().split(' '))
m = max(arr) +1
count = [0]* m

for a in arr:
	count[a] +=1

print count.index(max(count))