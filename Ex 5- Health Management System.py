# client Harry Rohan and Saurabh
# Each client have Diet and Excercise which will be lock in files, so total 6 files will generate.
# one function to retrive excercise and diet of clients

def getdate():
    import datetime
    return datetime.datetime.now()

def lock(player):
    if player ==1:
        type = int(input("1. for Excercise \n2. for Diet"))
        if type == 1:
            f = open("rohan_lock_exer.txt", "w+")
            excer = input()
            f.write(str(getdate()) + excer)
        elif type ==2:
            f = open("rohan_lock_diet.txt", "w+")
            diet = input()
            f.write(str(getdate()) +diet)

    elif player ==2:
        type = int(input("1. for Excercise \n2. for Diet"))
        if type == 1:
            f = open("saurabh_lock_exer.txt", "w+")
            excer = input()
            f.write(str(getdate()) + excer)
        elif type == 2:
            f = open("saurabh_lock_diet.txt", "w+")
            diet = input()
            f.write(str(getdate()) + diet)
    elif player == 3:
        type = int(input("1. for Excercise \n2. for Diet"))
        if type == 1:
            f = open("harry_lock_exer.txt", "w+")
            excer = input()
            f.write(str(getdate()) + excer)
        elif type == 2:
            f = open("harry_lock_diet.txt", "w+")
            diet = input()
            f.write(str(getdate()) + diet)

def retrieve(player):
    if player == 1:
        type=int(input("What you want to retrieve- \n1 for Excercise \n2 for Diet"))
        if type ==1:
            f = open("rohan_lock_exer.txt", "r")
            content = f.read()
            print(content)
        else:
            f = open("rohan_lock_diet.txt", "r")
            content = f.read()
            print(content)
    elif player == 2:
        type = int(input("What you want to retrieve- 1 for Excercise \n2 for Diet"))
        if type == 1:
            f = open("saurabh_lock_exer.txt", "r")
            content = f.read()
            print(content)
        else:
            f = open("saurabh_lock_diet.txt", "r")
            content = f.read()
            print(content)
    else:
        type = int(input("What you want to retrieve- 1 for Excercise \n2 for Diet"))
        if type == 1:
            f = open("harry_lock_exer.txt", "r")
            content = f.read()
            print(content)
        else:
            f = open("harry_lock_diet.txt", "r")
            content = f.read()
            print(content)

print("Welcome to Health Management System")
lock_ret = int(input("What you want lock or retrieve-- \n1 for Lock \n2 for retrive"))

if lock_ret ==1:
    player = int(input("For whom to lock- \n1. for Rohan \n2. for Saurabh \n3. for Harry"))
    lock(player)
else:
    player = int(input("For whom to Retrieve- \n1. for Rohan \n2. for Saurabh \n3. for Harry"))
    retrieve(player)





