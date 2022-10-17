f = open(r"elif.png", "rb")
s = f.read()
f.close()

rowList = []
for value in s:
    rowList.append(value )
rowList.reverse()


f = open(r"x.txt", "wb")

for value in rowList:
    f.write(value)
f.close()