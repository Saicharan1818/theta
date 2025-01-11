#with the help of iter keyword we can store the data of list and dictionaries---------###ITERATOR


#GENERATOR uses yield keyword

#Generator

def square(i):
#0,1,2,3,4,5,6,7,8,9
    for i in range(i):
        if i>5:
            print(i)
        yield i
square(10)
for i in square(10):
    print(i)

''''#DECORATOR using other function code into our code'''

def dev_dec(func):
    def inner(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return inner
@dev_dec
def div(a,b):
    if a < b:
        a,b = b,a
    return a / b

div(2,4)
div(4,2)
