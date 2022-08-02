#  write a python program to find the list in a list of list whose sum of element is the highest.

list=[1,2,3],[4,5,6],[10,11,12],[7,8,9]
i=0
while i<len(list):
    j=0
    a=[]
    while j<len(list[i]):
        a.append(sum(list[j]))
        j+=1
    i+=1
k=0
while k<len(list):
    if sum(list[k])==max(a):
        print(list[k])
    k+=1