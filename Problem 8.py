import random

def isCorrect(table,num):
    correctTable = []
    for i in range(1,11):
        correctTable.append(num*i)
    print("Correct table is-\n",correctTable)

    twoTable = zip(table,correctTable)
    dictable = dict(twoTable)
    # print("Result of zip- ",dictable)
    index = 1
    for key, value in dictable.items():
        if key == value:
            index+=1
        else:
            print("Table wrong at index ",index)
            index += 1

def rohanMultiplication(num):
    rohanTable = []
    wrong = random.randint(0, 9)
    print("wrong place", wrong)

    for i in range(1,11):
        if i == wrong:
            rohanTable.append((i*num)+1)
        else:
            rohanTable.append(i*num)
    return  rohanTable

if __name__ == '__main__':
    num = int(input("Enter the table by Rohan Das - "))
    table = rohanMultiplication(num)
    print(table)

    check = isCorrect(table,num)

