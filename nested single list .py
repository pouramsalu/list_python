# num=['a','b',['c',['d','e'],['j','g'],'k'],'l','m','n']
# i=0
# b=[]
# while i<len(num):
#     if type(num[i])==type([]):
#         j=0
#         while j<len(num[i]):
#             if type(num[i][j])==type([]):
#                 k=0
#                 while k<len(num[i][j]):
#                     b.append(num[i][j][k])
#                     k+=1
#             else:
#                 b.append(num[i][j])
#             j+=1
#     else:
#         b.append(num[i])
#     i+=1
# print(b)

list=[1,2,3],[4,5,[6,7],[8,9,10],[11,12,13]]
i=0
b=[]
while i<len(list):
    if type(list[i])==type([]):
        j=0
        while j<len(list[i]):
            if type (list[i][j])==type([]):
                k=0
                while k<len(list[i][j]):
                    b.append(list[i][j][k])
                    k+=1
            else:
                b.append(list[i][j])
            j+=1
    else:
        b.append(list[i])
    i+=1
print(b)