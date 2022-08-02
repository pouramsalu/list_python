# REMOVE DUPLICATE
list=['a',17,12,'a',17,18,'b',17,14,12,19,'b',12,13,11]
b=[]

i=0
while i < len(list):
    if list[i] not in b:
        b.append(list[i])
    i=i+1
print(b)


# REMOVE DUPLICATE AND PRINT AQLPHABETS AND NUMBER..
# a=['a',17,12,'a',17,18,'b',17,14,12,19,'b',12,13,11]
# b=[]
# c=[]
# i=0
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     else:
#         if a[i] not in c and a[i]==str(a[i]):
#             c.append(a[i])
#         i=i+1
# print(b)
# print(c)
