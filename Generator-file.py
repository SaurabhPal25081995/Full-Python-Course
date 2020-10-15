def gen(n):
    for i in range(n):
        yield i
g = gen(5)
print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())


# # Factorial by generator
# num = int(input("Enter the number "))
# def factgen(num):
#     fact = 1
#     for i in range(num):
#         fact = fact*(i+1)
#         yield fact
#
# g = factgen(num)
# print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

