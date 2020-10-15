# List Comprehension
# ls = [i for i in range(100) if i%3 == 0]
# print(ls)
#
# ls = [i for i in range(0,100,3) ]
# print(ls)
#
# # Print dictionary 0:item0, 1:item1..
# dict = { i:f"item{i}" for i in range(5) }
# print(dict)
#
# # Reverse of above dict
# dict1 = {value:key for key,value in dict.items()}
# print(dict1)

# Generator Comprehension
# evens = (i for i in range(40) if i%2==0)
# print(evens)
# print(type(evens))
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())

#Q Take numbers in input as a list, ask for which type of comprehension want ??
# ..convert them to that comprehension.

lst = input("Enter the number")
lst = lst.split(' ')
# print(type(lst))
# print(lst)
# lst=[i for i in input("enter element").split(' ')]

choice = int(input("Enter -\n 1 for List comprehension \n 2 for Set comprehension \n 3 for Dictionary comprehension"))
if choice ==1:
    lst1 = [i for i in lst]
    print(lst1)
elif choice == 2:
    sett = { i for i in lst}
    print(sett)
else:
    dict_user = {l: f"You are awesome programmer" for l in lst}
    print(dict_user)

