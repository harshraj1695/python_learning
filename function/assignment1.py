def count_max(lis,size):
    count=0
    for i in lis:
        if(len(i)>size):
            count+=1
    print("count of numver with char count more than size is ",count)


lis=[]
n=int(input("enter the number of person you want to enter: "))
for i in range(n):
    name=input("enter the name of person: ")
    lis.append(name)

size=int(input("enter the max char count "))

count_max(lis,size)