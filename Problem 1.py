"""The task you have to perform is “Your Age In 2090”. This task consists of a total of 10 points to
evaluate your performance.

Problem Statement:-
Take age or year of birth as an input from the user. Store the input in one variable.
Your program should detect whether the entered input is age or year of birth and tell the user when
they will turn 100 years old. (5 points).

Here are a few instructions that you must have to follow:

Do not use any type of modules like DateTime or date utils. (-5 points)
Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
Your code should handle all sort of errors like:                       (2 points)
You are not yet born
You seem to be the oldest person alive
You can also handle any other errors, if possible!"""

num = int(input("Enter your age or year"))
if num in range(5,151):
    print("You will turn 100 year old in -",(2020-num)+100)

elif num > 151 and num < 250:
    print("YOu seem to be the oldest person alive")

elif  num in range(1900,2020):
    print("Your age is - ",2020-num)
    print("You will turn 100 year old in - ",num+100)

elif num > 2020:
    print("You are not yet born")