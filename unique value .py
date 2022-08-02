n=[1,2,2,5,8,4,4,8]
a=[]
count=0
i=0
while i<len(n):
    if n[i]not in a:
        a.append(n[i])
        count+=1
    i=i+1
print("unique value=",a)
print("count=",count)


# string=input("enter the string")
# i=0
# while i<len(string):
#     j=0
#     while j<len(string):
#         print(string[i:],end=" ")
#         j+=1
#     i+=1

