# write a python program to split a list every Nth element.
# expected output=[['a','d','j','m'],['b','e','h','k','n']['c','f','i','l']]

list=['a','b','c','d','e','f','g','h','i','i','j','k','l','m','n']
b=[]
i=0
a=3
while i<=a:
    b.append(list[i::a])
    i=i+1
print(b)


  
