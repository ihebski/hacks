symbols = '!#$%&()*+,-./'

# company.2017
def gen1(ch,c):
	return [ch+c+str(i) for i in range(1930,2020)]

# company2017.
def gen2(ch,c):
	return [ch+str(i)+c for i in range(1930,2020)]

# company2017
def generateDate(ch):
	return [ch+str(i) for i in range(1930,2020)]


if __name__ == '__main__':
	print "======== LaZy G3nerat0r ======"
	companyName = raw_input("company name : ")
	save = open(companyName+".txt","a")
	save.write("\n".join(generateDate(companyName)))
	save.write("\n".join(generateDate(companyName.upper())))
	
	for x in list(symbols):
		# LowerCase
		save.write("\n".join(gen1(companyName,x)))
		save.write("\n".join(gen1(companyName.title(),x)))
		save.write("\n".join(gen1(companyName.upper(),x)))
				
		# Upper case
		save.write("\n".join(gen2(companyName,x)))
		save.write("\n".join(gen2(companyName.title(),x)))
		save.write("\n".join(gen2(companyName.upper(),x)))
	print "Wordlist name is : ",companyName+".txt"	
	print "Number of lines generated is : ",sum(1 for line in open(companyName+".txt"))