enc ="E4A5D4A1C3C4D4B3A5D2D3B4C2C5C1A5C2C4C3C4A1C1C5B3A1A2A5D4B4A3D3D5A2D3D4B4D4D5D4B4C4C3A3B4C5B3A5D2"
A = ["A","B","C","D","E"]
B = ["F","G","H","I","K"]
C = ["L","M","N","O","P"]
D = ["Q","R","S","T","U"]
E = ["V","W","X","Y","Z"]
n = 2
k = [enc[i:i+n] for i in range(0, len(enc), n)]
flag = ""
for x in k:
	if x[0] =="A":
		flag += A[int(x[1]) -1]
	elif x[0] =="B":
		flag += B[int(x[1]) -1]
	elif x[0] =="C":
		flag += C[int(x[1]) -1]
	elif x[0] =="D":
		flag += D[int(x[1]) -1]
	elif x[0] =="E":
		flag += E[int(x[1]) -1]
print flag		



