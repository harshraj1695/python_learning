# class build:
#     share="shyam"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("name: {}, age: {}, share: {}".format(self.name, self.age, build.share))

# class build:
#     share="shyam"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         def display(self):
#           print("name: {}, age: {}, share: {}".format(self.name, self.age, build.share))
#         display(self)

class build:
    share="shyam"
    def __init__(self,name,age,share):
        self.name=name
        self.age=age
        self.share=share
    def display(self):
        print("name: {}, age: {}, share: {}".format(self.name, self.age, self.share))


b1=build("jii",243,"haaaaaa")
print(build.share)  #here share is class variable so we can access it by class name
b1.display()