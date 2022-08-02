# a=[1,2,4,5,7,9,11,12,15]
# i=1
# b=[]
# while i<=15:
#     j=0
#     if i not in a:
#         b.append(i)
#         j=j+1
#     i=i+1
# print(b)


list=[12,24,27,32,48,60,71,82,86,90,92,94,99]
i=0
b=[]
while i<=100:
    j=0
    if i not in list:
        b.append(i)
        j+=1
    i+=1
print(b)