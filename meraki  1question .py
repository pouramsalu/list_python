#  write a code that counts the number between 20 and 40 and then print its count

list=[50,40,23,70,56,12,5,10,7]
i=0
count=0
while i<len(list):
    if list[i]>=20 and list[i]<=40:
        count+=1
    i+=1
print(count)



