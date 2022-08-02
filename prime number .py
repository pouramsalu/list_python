

# i=1
# b=[]
# while i<=30:
#     j=2
#     count=0
#     while j<=i//2:
#         if i%j==0:
#             count+=1
#             break
#         j+=1
#     if count==0 and i!=1:
#         b.append(i)
#     i+=1
# print(b)



i=1
b=[]
while i<=100:
    j=2
    count=0
    while j<=i//2:
        if i%j==0:
            count+=1
            break
        j+=1
    if count==0 and i!=1:

        if i>11:
            x=i%10
            y=i//10
            z=str(x)+str(y)
            r=[i,int(z)]
            b.append(r)
    i+=1
print(b)

