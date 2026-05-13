from array import *
arr=array('i',[])

size=int(input("enter the size of array: "))

for i in range(size):
    x=int(input("enter the next element in array: "))
    arr.append(x)

print("the array is : ",arr)

# removing element at a specific index
index=int(input("enter the index to remove from: "))

if(index<0 or index>=len(arr)):
    print("invalid index")
else:
 index-=1
 for i in range(index,len(arr)-1):
    arr[i]=arr[i+1]
 arr.pop()
 print("the array after deletion is: ",arr)