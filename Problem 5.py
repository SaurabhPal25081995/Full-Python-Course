""""
Problem Statement:-
You are given a list that contains some numbers. You have to print a list of next palindromes only if
the number is greater than 10; otherwise, you will print that number.

Input:
[1, 6, 87, 43]

Output:
[1, 6, 88, 44]
"""

def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == "__main__":
    n = int(input("Enter the number of test cases\n"))
    numbers = []
    for i in range(n):
        number = int(input("Enter the number:\n"))
        numbers.append(number)

    for i in range(n):
        if numbers[i] < 10:
            print(f"Next palindrome for {numbers[i]} is {numbers[i]}")
        else:
            print(f"Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")
