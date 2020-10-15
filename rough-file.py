# # # print([i for i in range(0,int(input('enter no:')))])
# #
# # import re
# #
# # str = "saurabhpal25@gmail.com hi saurabh oak@yah  jio5@coo.com sfs  o@g.c sfd s gaga@gmail.com gs a s s s fsdfd fsd fsdffd"
# # x=re.findall(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+',str)
# # print(x)
# #
# # list1 = [1,2,3,4,5]
# # # rev = list1[:]
# # rev = list1.copy()
# # rev.reverse()
# # print(rev)
# # print(list1)
#
# # a = [11,22,3]
# # b = [4,51,60]
# # c = zip(a,b)
# # print(tuple(c))
#
# # str = "Saurabh is a software developer hbaruas"
# # print(str.strip("Saurabh"))
#
# # number = 2
# # table = [i * number for i in range(1, 11)]
# # print("table ",table)
# #
# # mytable=[]
# # num = 2
# # for i in range(1, 11):
# #     mytable.append(i * num)
# # print("mytable ",mytable)
# '''
# Python Practice problem 8 (Easy, 10 points)
# Rohan Das Is A Fraud
# Rohan das is a fraud by nature.
# Rohan Das wrote a python function to print a multiplication table of a given number and put one of the values (randomly generated) as wrong.
# Rohan Das did this to fool his classmates and make them commit a mistake in a test. You cannot tolerate this!
# So you decided to use your python skills to counter Rohan’s actions by writing a python program that validates Rohan’s multiplication table.
# Your function should be able to find out the wrong values in Rohan’s table and expose Rohan Das as a fraud.
# Note: Rohan’s function returns a list of numbers like this
# Rohan Das’s Function Input:
# rohanMultiplication(6)
# Rohan’s function returns this output:
# [6, 12, 18, 26, …., 60]
# You have to write a function isCorrect(table, number) and return the index where rohan’s function is wrong and print it to the screen! If the table is correct, your function returns None.
# '''
# import random
#
# def rohanMultiplication(number):
#     wrong = random.randint(0, 9)
#     table = [i * number for i in range(1, 11)]
#     table[wrong] = table[wrong] + random.randint(0, 10)
#     return table
#
# def isCorrect(table, number):
#     for i in range(1, 11):
#         if table[i - 1] != i * number:
#             return i - 1
#     return None
#
# if __name__ == "__main__":
#     # print(rohanMultiplication(7))
#     number = int(input("Enter a number: "))
#     myTable = rohanMultiplication(number)
#     print(myTable)
#     wrongIndex = isCorrect(myTable, number)
#     print(f"The table is wrong at index {wrongIndex}")
#
#
#
#



# n = 20
#
# i = 0
# # guess = []
# chance = 5
# count = 0
# while True:
#     user = int(input('Input the number:'))
#
#     if user>n:
#         print('number is greater')
#         # guess.append(user)
#         count +=1
#         chance = chance-1
#         print('no of guess',count)
#         print("no of chances left", chance)
#
#
#
#     elif user<n:
#         print('number is smaller')
#         guess.append(user)
#         y = len(guess)
#         print("guess count",y)
#
#     else user==18:
#         print('entered is correct')
#
#


import random

'''
Author : jayesh kaushik
program : Jumble words
Code for : CodeWithHarry(Practice problem 9)
This function is used for to jumble the words
'''


# def jumble_word(first_name, lastt_name, number):
#     for i in range(0, number):
#         # Changing the last name
#         joumbled_name = first_name[i] + " " + lastt_name[random.randint(0, number - 1)]
#         print(joumbled_name)


# if __name__ == "__main__":
#     # Length of the name list
#     number = int(input("Enter the number of names:\n"))

#     nameList = []
#     first_name = []
#     lastt_name = []

#     # Asking the name of the friends
#     for i in range(1, number + 1):
#         name = input("Enter the name:")
#         # append to the name list
#         nameList.append(name)

#     # Spliting the elements of the name list
#     for ele in nameList:
#         split_name = ele.split(" ")
#         # For the first name
#         first_name.append(split_name[0])
#         # For the second name
#         lastt_name.append(split_name[1])

#     jumble_word(first_name, lastt_name, number)


import pdb
pdb.set_trace()

name = input("Enter your name")
age = int(input("Enter your age"))
age +=5
print(age)












