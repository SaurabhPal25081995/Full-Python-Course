num1 = input("Enter the first no")
num2 = input("Enter the next no")

try:
    print("Sum of two no. is ",int(num1)+int(num2))
except Exception as e:
    print(e)
finally:
    print("Most important line")