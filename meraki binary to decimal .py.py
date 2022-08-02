# b=[1,0,0,1,1,0,1,1]
# i=len(b)-1
# c=1
# decimal=0
# while i>=0:
#     decimal=decimal+b[i]/c
#     c=c/2
#     i-=1
# print("decimal",decimal)


list=[1,0,0,1,1,1]
i=len(list)-1
c=1
decimal=0
while i>=0:
    decimal=decimal+list[i]/c
    c=c/2
    i-=1
print("decimal",decimal)


