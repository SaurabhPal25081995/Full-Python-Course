# Pattern is n = no. of rows
"""
*****
****
***
**
*
"""

row = int(input("Enter no. of rows "))
bol = input("Type 1 for True, 0 for False")
var = bool(bol)
print(bol)

if bol==True:
    for i in range(0,row):
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")
else:
    for i in range(0, row):
        for j in range(row, i, -1):
            print("* ", end="")
        print()
