# Duplicates

# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# a=[]
# b=[]
# i=0
# while i<len(n):
#     if n[i] not in a:
#         a.append(n[i])
#     else:
#         if n[i] not in b:
#             b.append(n[i])
#     i=i+1
# print(b) 


list=[12,22,34,12,22,22,12,34,22,34]
a=[]
b=[]
i=0
while i<len(list):
    if list[i]not in a:
        a.append(list[i])
    else:
        if list[i]not in b:
            b.append(list[i])
    i+=1
print(b)