class unknow:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def __str__(self):
        return "name: {}, age: {}".format(self.name, self.age)
    
u1=unknow("harsh", 24)
print(u1)  #it will print the address of the object but if we want to
#                    print the value of the object then we have to override 
#                      the __str__ method and return the string

print(type(u1))  #it will return the class of the object

