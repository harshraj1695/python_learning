class phone:

    def show(self):
        print("this is parent class")

class smartphone(phone):

    def show(self):
        print("this is child class")


s1=smartphone() #this is method overriding
s1.show()


# parent version
phone.show(s1)