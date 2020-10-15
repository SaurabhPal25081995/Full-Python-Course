# Decorator is callable object, used when we have do same task with multiple function.

# def function1():
#     print("Hi-----")
#
# func2 = function1
# del function1
# func2()

def deco1(func1):
    def nowexc():
        print("Executing now")
        func1()
        print("Executed")
    return nowexc

@deco1
def who_is_pal():
    print("Pal is the surname")

#who_is_pal = dec1(who_is_pal) # This line is equivalent to @deco1
who_is_pal()