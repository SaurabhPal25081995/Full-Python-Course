# Faulty Calculator

print("Enter the first no.")
num1 = int(input())
print("Enter next no.")
num2 = int(input())
print("Enter the operation")
op = input()

if (num1 == 45 and num2 ==3) or (num1==3 and num2==45) and op == "*":
    print("555")
elif (num1 == 56 and num2 ==9) or (num1==9 and num2==56) and op == "+":
    print("77")
elif (num1 == 56 and num2 ==6)  and op == "/":
    print("4")
elif op=="+":
    print(num1+num2)
elif op=='-':
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
