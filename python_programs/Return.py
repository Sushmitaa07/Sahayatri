#Return
def add():
    a=10
    b=20
    c=a+b
    return c
print (add())

#Nested function:
def outer (a,b):
    c=a+b
    def inner()
        d=1
        return d
    return c+inner()
print(outer(10,20))

def outer(sum):
    def inner():
        d=sum()
        return d+1
    return inner()
def sum(a=10,b=20):
    c=a+b
    return c
e=outer(sum)
print(e)

#Enclosing name space:
b=20
def outer():
    c=100
    def inner():
        a=10
        print(a)
        print(c)


