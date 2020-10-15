import random
import datetime

def guess_num(a,b,num):
    count = 0
    f = open("problem6.txt","a")
    guess = int(input(f"Guess the number between {a} and {b} "))

    while guess != num:
        if guess > num:
            # print("Wrong! Guess a  smaller number, Try Again !!!")
            guess = int(input(f"Enter a smaller number\n"))
            count+=1
            f.write(str(datetime.datetime.now()))

        elif guess < num:
            # print("Wrong! Guess a  greater number, Try Again !!!")
            guess = int(input(f"Enter a bigger number\n"))
            count+=1
            f.write(str(datetime.datetime.now()))

        else:
            count +=1
            print(f"Correct you took {count} trails")
            f.write(str(datetime.datetime.now()))
            break
    return count

if __name__ == "__main__":
    a = int(input("Enter value of a "))
    b = int(input("Enter value of b "))
    num1 = random.randint(a,b)
    num2 = random.randint(a,b)
    # print(num1)
    # print(num2)
    print("Player1 chance---")
    player1 = guess_num(a,b,num1)
    print("Player2 chance-----------------")
    player2 = guess_num(a,b,num2)

    print(f"Player1 took {player1} chance while Player2 took {player2} chance")
    if player1 > player2:
        print("Player2 Won")
    elif player1 < player2:
        print("Player1 Won")
    else:
        print("Tie!!!")



