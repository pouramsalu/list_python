n=2
m=9
list=[2,9]
c=[]
i=0
while i<len(list):
    j=0
    while j<len(list):
        if list[i] not in c:
            c.append(list[i])
        j=j+1
    i=i+1
k=0
while k<len(c):
    if c[k]>0:
        if c[k]%2==0:
            sum=c[k]
        k+=1
    print(sum)