num1 = input("Enter your input - ")
num1 = list(num1)
num2 = num1.copy()

last = len(num2)
for i in range(last//2):
    temp = num2[i]
    num2[i] = num2[last-1]
    num2[last - 1] = temp
    last=last-1

if num2 == num1:
    print(f" {num2} input is palindrome")
else:
    print(f"Your input is not palindrome")