# list=[1,2,3,4,1,2,3,4,5,6,7]
# i=0
# a=[]
# sum=0
# while i<len(list):
#     if list[i] not in a:
#         a.append(list[i])
#     i=i+1
# print(a)


list=[1,2,1,2,3,2,3,4,5,1,2,3,4,5,6,7,5,6,7,8,9,10]
i=0
a=[]
# sum=0
while i<len(list):
    if list[i]not in a:
        a.append(list[i])
    i+=1
print(a)