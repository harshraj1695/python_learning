class Demo:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"

d = Demo()

print(d.public)        # works
print(d._protected)    # works

# print(d.__private)   # error

print(d._Demo__private)   # works internally