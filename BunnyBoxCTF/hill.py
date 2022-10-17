import numpy as np
global debug,alphabet,alphsize
debug=0
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789_{}"
alphsize=len(alphabet)
 
def modMatInv(A,p):       # Finds the inverse of matrix A mod p
    n=len(A)
    A=np.matrix(A)
    adj=np.zeros(shape=(n,n))
    for i in range(0,n):
        for j in range(0,n):
            adj[i][j]=((-1)**(i+j)*int(round(np.linalg.det(minor(A,j,i)))))%p
    return (modInv(int(round(np.linalg.det(A))),p)*adj)%p
 
def modInv(a,p):          # Finds the inverse of a mod p, if it exists
    for i in range(1,p):
        if (i*a)%p==1: return i
    raise ValueError(str(a)+" has no inverse mod "+str(p))
 
def minor(A,i,j):    # Return matrix A with the ith row and jth column deleted
    A=np.array(A)
    minor=np.zeros(shape=(len(A)-1,len(A)-1))
    p=0
    for s in range(0,len(minor)):
        if p==i: p=p+1
        q=0
        for t in range(0,len(minor)):
            if q==j: q=q+1
            minor[s][t]=A[p][q]
            q=q+1
        p=p+1
    return minor
 
 
 
def encrypt(msg, key, sz):
    triple = [list(msg[i*sz:(i*sz)+sz]) for i in range(0, len (msg)/sz)]
    if debug>0: print triple
    mul = [i[:] for i in triple]
    for x in range(len(triple)):
        for i in range(len(triple[x])):
            # triple[x][i]=ord(triple[x][i])-65
            triple[x][i]=alphabet.find(triple[x][i])
    if debug>0: print triple
    for x in range(len(triple)):
        mul[x] = np.dot(key,triple[x]) % alphsize
    if debug>0: print mul
    enc=""
    for x in range(len(mul)):
        for s in range(0,sz): enc+=alphabet[mul[x][s]]
    return enc
 
def decrypt(msg, key, sz):
    try: deckey = modMatInv(key,alphsize)
    except ValueError: return
    triple = [list(msg[i*sz:(i*sz)+sz]) for i in range(0, len (msg)/sz)]
    mul = [i[:] for i in triple]
    for x in range(len(triple)):
        for i in range(len(triple[x])):
            # triple[x][i]=ord(triple[x][i])-65
            triple[x][i]=alphabet.find(triple[x][i])
    if debug>0: print triple
    for x in range(len(triple)):
        mul[x] = np.dot(deckey,triple[x]) % alphsize
    if debug>0: print mul
    dec=""
    for x in range(len(mul)):
        for s in range(0,sz): dec+=alphabet[int(mul[x][s])]
    return dec
 
 
encr="DKBRHSBTJVPHFKYJASSTZBOCOXXMRCKTNRJGGRSCBQJBRZVKPGAJOVANNEIHIKITIHKHUOFYISZBOCSIGEXQZYWEFANOAVEWQBJNYVUUYEAOIRRSWY"
correctkey = [[3,2,7], [4,5,6], [1,9,8]]
correctkey= np.transpose(correctkey)
sz=len(correctkey)
msg="jackandjillwentupthehilltofetchapailofwaterjackfelldownandbrokehiscrownandjillcametumblingaftertheflagiscymopoleia"
print encrypt(msg,correctkey,sz)
print decrypt(encrypt(msg,correctkey,sz),correctkey,sz)
 
matrix = [[54, 53, 28, 20, 54, 15, 12, 7],
          [32, 14, 24, 5, 63, 12, 50, 52],
          [63, 59, 40, 18, 55, 33, 17, 3],
          [63, 34, 5, 4, 56, 10, 53, 16],
          [35, 43, 45, 53, 12, 42, 35, 37],
          [20, 59, 42, 10, 46, 56, 12, 61],
          [26, 39, 27, 59, 44, 54, 23, 56],
          [32, 31, 56, 47, 31, 2, 29, 41]]
 
 
 
ciphertext = "7Nv7}dI9hD9qGmP}CR_5wJDdkj4CKxd45rko1cj51DpHPnNDb__EXDotSRCP8ZCQ"
print encrypt("IceCTF{l",matrix,8)
print decrypt(ciphertext,matrix,8)