def dev_dec(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner

@dev_dec
def div(a, b):
    return a / b

result1 = div(2, 4) 
result2 = div(4, 2) 

print("div(2, 4) =", result1) 
print("div(4, 2) =", result2)