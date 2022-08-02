money= [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
thousand=0
lakh=0
crore=0
while i<len(money):
    if money[i]>=100 and money[i]<100000:
        thousand+=1
    elif money[i]>=100000 and money[i]<10000000:
        lakh+=1
    else:
        crore+=1
    i+=1
print("money in thousand:",thousand)
print("money in lakh:",lakh)
print("money in crore:",crore)