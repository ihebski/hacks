def qsort(arr):
	less = []
	equal = []
	greater = []
	if len(arr)>1:
		pivot = arr[0]
		for x in arr:
			if x == pivot:
				equal.append(x)
			if x> pivot:
				greater.append(x)
			if x < pivot:
				less.append(x)
		return less+equal+greater				


m = input()
ar = [int(i) for i in raw_input().strip().split()]


for x in qsort(ar):
	print x,