# Write a code that works for any list, it shows the two averages as the output. One is the average of even numbers and the other is the average of odd numbers from the given list.

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even=0
sum=0
sum1=0
odd=0
while i <len(elements):
    if elements [i]%2==0:
        even+=1
        sum+=elements[i]
        average=sum/even
    else:
        odd+=1
        sum1+=elements[i]
        average1=sum/odd
    i=i+1
print("average of even no:",average)
print("average of odd numbe:",average1)

