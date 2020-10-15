
# By iterative method
# n=int(input("Enter the terms"))
# a=0                                         #first element of series
# b=1                                         #second element of series
# if n<=0:
#     print("The requested series is",a)
# else:
#     print(a,b,end=" ")
#     for x in range(2,n):
#         c=a+b
#         print(c,end=" ")
#         a=b
#         b=c

# By Recursion
def fib(n):
   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))
# take input from the user
nterms = int(input("How many terms? "))
# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(fib(i),end=" ")