# name=[]
# size=int(input("enter the size of string:"))
# i=0
# while i<(size):
#     a=input("enter the character:")
#     name.append(a)
#     i+=1
# b=[]
# i=-1
# while i>=-(len(name)):
#     b.append(name[i])
#     i-=1
# print(b)
# if b==name:
#     print("palindrome")
# else:
#     print(" not palindrome")


s=input("enter any string")
l=list(s)
a=len(l)
i=-1
n=[]
while i>=-a:
    n.append(l[i])
    i-=1
if n==l:
    print("palindrome")
else:
    print("not palindrome")
print(n)