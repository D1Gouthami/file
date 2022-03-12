f=open ("t.txt","w")
b=["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
i=0
while i<len(b):
    f.write(b[i])
    f.write("\n")
    i+=1
f.close()
