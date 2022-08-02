



# list=[[1,2,3],[4,5,6],[10,11,12],[7,8,9]]
# i=0
# while i<len(list):
#     j=0
#     a=[]
#     while j<len(list[i]):
#         a.append(sum(list[j]))
#         j+=1
#     i+=1

# k=0
# while k<len(list):
#     if sum(list[k])==max(a):
#         print(list[k])
#     k+=1

# list1=[1,3,4,5,6,7,8,9]
# i=0
# a=[]
# while i<len(list1):
#     c=[]
#     c.append(list1[i])
#     c.append(list1[i+1])
#     a.append(c)
#     i+=2
# print(a)


# list=[[10,11,12,[13,14,15],16,[17],18,19]]
# a=list[0][4]
# b=list[0][3][0]
# c=list[0][2]
# print(a,",",b,",",c)

# list=[2,4,8,[9],10,11,[12,13,14],15]
# a=list[3]
# b=list[6][1]
# c=list[2]
# print(a,b,c)

# list=[0,1,2,[3],5,[4],6,[7],[8,9,10]]
# a=list[5]
# b=list[8][1]
# c=list[8][2]
# d=list[4]
# print(a,",",b,",",c,",",d)

# list=[2,3,9,10,[1,2,33,34,43,],[13,[4,[4,6,7]]]]
# a=list[5][1][1][1]
# b=list[4][4]
# c=list[5][0]
# d=list[3]
# e=list[5][1][1][2]
# print(a,",",b,",",c,",",d,",",e)

# list=[[1,2],[5,8],[4,7],[3,9],[12,81]]
# a=list[0][1]
# b=list[1][1]
# c=list[2][0]
# d=list[4][0]
# print(a,",",b,",",c,",",d)

# a=[9.0, "soso","narani",16,9,6.7]
# i=0
# a1=[]
# b=[]
# c=[]
# while i<len(a):
#     if (type(a[i])==int):
#        a1.append(a[i])
#     elif (type(a[i])==str):
#         b.append(a[i])
#     elif (type(a[i])==float):
#         c.append(a[i])
#     i=i+1
# print(a1,"\n",b,"\n",c)

# a=[1,2,3]
# b=[5,6,7]
# i=0
# while i<len(a):
#     i=i+1
# print(a+b)

list=[[1,2],[5,8],[4,7],[3,9],[12,81]]  
i=0
b=[]
while i<len(list):
    j=0
    while j<len(list[i]):
        e=(list[i][j])
        # if e%2!=0:
        b.append(e)
        j=j+1
    i=i+1
print(b)
