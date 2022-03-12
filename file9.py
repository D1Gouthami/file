obj=open("gou.txt","r")
a=[1,2,3,4,5]
i=0
c=0
while i<len(a):
    c+=1
    i+=1
obj.read()
print(c)
obj.close()