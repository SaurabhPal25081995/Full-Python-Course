"""Problem Statement:-
You visited a restaurant called CodeWithHarry, and the food items in that restaurant are sorted,
based on their amount of calories. You have to reserve this list of food items containing calories.
You have to use the following three methods to reserve a list:

Inbuild method of python
List name [::-1] slicing trick
Swapping the first element with the last one and second element with second last one and so on like,
[6 7 8 34 5] -> [5 34 8 7 6]

Input:
Take a list as an input from the user
[5, 4, 1]

Output:
[1, 4, 5]
[1, 4, 5]
[1, 4, 5]
All three methods give the same results!"""


lst =[1,2,3,4,5]

list1 = lst[:]
list1.reverse()
print("Original list - ",lst)
print("First reverse list - ",list1)


lst2 = lst[::-1]
print("Second reverse list - ",lst2)

last = len(lst)
for i in range(last//2):
    temp = lst[i]
    print("Temp",temp)
    print("Last",lst[last-1])

    lst[i] = lst[last-1]
    lst[last - 1] = temp
    last=last-1
    print(lst)

if lst == list1 and list1 == lst2:
    print("All are working properly")