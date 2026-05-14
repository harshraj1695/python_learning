def add(x,y):
    return x+y

#variable length args

def add(*args):
    sum=0
    for i in range(len(args)):
        sum+=args[i]
    return sum

def pri(x,name):
    print(x,name)

# keyword variable length args
def info(**kwargs):
    print(kwargs)

info(name="Harsh", age=21)
print(add(1,2))
print(add(1,2,3,4,5))
pri(1,name='harsh')