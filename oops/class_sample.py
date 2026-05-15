
# from random import sample


class simple:
    def __init__(self, name, age, rollno):
        self.name = name
        self.age = age
        self.rollno = rollno
    
    def display(self):
        print("Name: {}, Age: {}, rollno: {}".format(self.name, self.age, self.rollno))
        # print("Name: {}, Age: {}, rollno: {}", self.name, self.age, self.rollno)  # -> it will print like this Name: {}, Age: {}, rollno: {} john 1001 20 

sample1=simple("john", rollno=20, age=1001)

sample1.display()