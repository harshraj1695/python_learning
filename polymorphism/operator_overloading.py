
class student:

    def __init__(self, mark1, mark2):
        self.mark1=mark1
        self.mark2=mark2

    def __add__(self,other):
        s2=student(0,0)
        s2.mark1=self.mark1+other.mark1
        s2.mark2=self.mark2+other.mark2
        return s2
    

s1=student(80,90)
s2=student(70,60)

s3=s1+s2  #it will call the __add__ method and return the object of student class (operator overloading)
print(s3.mark1)  #it will print the sum of mark1 of s1 and s2
print(s3.mark2)  #it will print the sum of mark2 of s1 and s2
