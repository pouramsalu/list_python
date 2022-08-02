#*** Append:Add and elements at the end of the list.

# list=["a","b","c","d"]
# list.append("e")
# print(list)


# clear:removes all the element from the list.

# list=["a","b","c"]
# list.clear()
# print(list)


# extend:add the element of the list,to the end of the current list

# list=["a","b","c"]
# n=[1,2,3]
# list.extend(n)
# print(list)

# insert:adds the elements at the specified position.

# list=["a","b","c"]
# list.insert(2,"e")
# print(list)

# pop:remove the elements at the specified position.

# pop=[1,2,3,4,5]
# list.pop(4)
# print(list)

# remove:removes the items with the specified value.
# list=["a","b","c"]
# list.remove("a")
# print(list)

# reverse:reverse the order of the list.
# list=[1,2,3,4,5]
# print(list[::-1])


# sort:sort the list
list=[1,4,6,3,2]
list.sort()
print(list)

# index:return the index of the first value.
a=[2,3,4,7,8]
print(a[0])

# str2="hello"
# str2ist=list(str2)
# print(str2ist)

# a=[1,2,3,4,5]
# print(a)
# a[1]=5
# a[4]=2
# print(a)

a=[12,56,9,36,24]
i=-1
while i>=-(len(a)):
    print(a[i],end=" ")
    i=i-1
