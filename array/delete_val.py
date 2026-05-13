
from array import *
a=array('i', [])
size=int(input("enter the sieze of the array: "))

for i in range(size):
   x=int(input("enter the element: "))
   a.append(x)

print("the array is: ",a)

val =int(input("enter the value to delete:  "))

for i in range(len(a)):
   if(a[i]==val):
      for j in range(i,len(a)-1):
         a[j]=a[j+1]
      a.pop()
      break
print("the array after deletion is: ",a)



