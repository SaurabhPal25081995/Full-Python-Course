
"""
Problem Statement:-
Harry Potter has got the “n” number of apples. Harry has some students among whom he wants to distribute the apples.
These “n” number of apples is provided to harry by his friends, and he can request for few more or few less apples.
You need to print whether a number is in range mn to mx, is a divisor of “n” or not.

Input:
Take input n, mn, and mx from the user.

Output:
Print whether the numbers between mn and mx are divisor of “n” or not. If mn=mx, show that this is not a range, and mn is equal to mx. Show the result for that number.

Example:
If n is 20 and mn=2 and mx=5
2 is a divisor of20
3 is not a divisor of 20
…
5 is a divisor of 20
"""
n = int(input("Enter the no. of apples"))
min = int(input("Enter the lowest value of distribution"))
max = int(input("Enter the largest value of distribution"))

if min == max:
    print("This is not a range")
    if n % min == 0:
        print(f"{min} is a divisor of {n}")
    else:
        print(f"{min} is not a divisor of {n}")

else:
    for i in range(min,max+1):
        if n % i == 0:
            print(f"{i} is a divisor of {n}")
        else:
            print(f"{i} is not a divisor of {n}")
