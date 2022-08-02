# write a code that print the maximum in this list:with method....****

# list=[50,40,23,70,56,12,5,10,7]
# i=0
# while i<len(list):
#     i+=1
# print(max(list))


list=[50,40,23,70,56,12,5,10,7]
i=0
max=0
while i<len(list):
    if list[i]>max:
        max=list[i]
    i=i+1
print(max)