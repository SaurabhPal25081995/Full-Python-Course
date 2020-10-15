def calc(a,b):
    ''' Addition of two numbers'''
    print("In calc func")
    sum = a+b
    return sum

v=calc(3,2)
print(v)
print(calc.__doc__)