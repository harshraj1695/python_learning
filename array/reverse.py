
from array import *
arr=array('i',[])
size=int(input("enter the size of array: "))
for i in range(size):
    x=int(input("enter the next element in array: "))
    arr.append(x)

print("the array is ",arr)

# revesing the array
i=0
j=len(arr)-1
while(i<j):
    arr[i],arr[j]=arr[j],arr[i]
    i+=1
    j-=1

print("the reversed array is ",arr)