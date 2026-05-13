from array import *

arr=array('i',[])
size=int(input("enter the size of array: "))
for i in range(size):
    x=int(input("enter the nex element in the array: "))
    arr.append(x)
print("the array is ",arr)

# binary search logic for a sorted array

key=int(input("enter the element to search: "))

low=0
hight=len(arr)-1
while(low<=hight):
    mid=(low+hight)//2
    if(arr[mid]==key):
        print("element found at index ",mid)
        break
    elif(arr[mid]<key):
        low=mid+1
    else:
        hight=mid-1

