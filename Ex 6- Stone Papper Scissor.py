import random
print("Welcome to Stone Paper scissor Game")
i=0
user_win=0
pc_win=0
draw =0
while(i<10):
    lst = ["stone","paper","scissor"]
    rand = random.choice(lst)
    user = input("Enter the your choice stone or paper or scissor - ")
    if rand == "stone" and user == "stone":
        print("Draw !!!")
        draw+=1
    elif rand == "stone":
        if user =="paper":
            print("You Win")
            user_win+=1
        elif user == "scissor":
            print("You Loss")
            pc_win+=1
    elif rand == "paper" and user == "paper":
        print("Draw!!!")
        draw += 1
    elif rand =="paper":
        if user == "stone":
            print("You Lost")
            pc_win += 1
        elif user == "scissor":
            print("You Win")
            user_win += 1
    elif rand =="scissor" and user == "scissor":
        print("Draw !!!")
        draw += 1
    elif rand =="scissor":
        if user =="stone":
            print("You Win")
            user_win += 1
        elif user =="paper":
            print("You Lost")
            pc_win += 1
    print("Computer system choose -",rand)
    i+=1

print(f"No of times You wins {user_win}")
print(f"No of times PC wins {pc_win}")
print(f"No. of time match Draw {draw}")
if user_win > pc_win:
    print("You Won the Match")
elif pc_win >user_win:
    print("You Lost the Match")
else:
    print("Draw !!!")



