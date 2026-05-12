a=int(input("Enter the first number: "))
b=int(input("enter the second number: "))
c=int(input("enter the third number: "))

grt=0;
if(a>b and b>c):
    grt=a;
elif(b>c and c>a):
    grt=b;
else:
    grt=c;
print("the greatest among the three is ",grt)