# a=[89,0,5,76,87,23]
# i=0
# while i<len(a):
#     a.sort
#     i+=1
# print("maximun number is:",a[-2])




# a= [50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# while i<len(a):
#     a.sort
#     i+=1
# print("maximum number is:",a[-2])

list=[50,40,23,70,56,12,5,10,7]
i=0
s=0
b=0
while i<len(list):
    if list[i]>b:
        b=list[i]
    if list[i]>s and list[i]!=b:
        s=list[i]
    i=i+1
print(s)
