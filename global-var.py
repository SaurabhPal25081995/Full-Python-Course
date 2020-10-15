x = 89
def harry():
    x = 20
    def rohan():
        global x
        x = 88
    print("Before calling rohan value of x", x)
    rohan()
    print("After calling rohan value of x", x)

harry()
print(x)