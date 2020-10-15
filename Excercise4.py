# Prgram of Guess,
# no. of guess 9
# print no. of guessess left
# No of guessess he took to finish
# game over if no. of guess end

#Let Guess num = 19
guess =9
while(True):
    print("Enter the guess no.")
    num = int(input())
    if num>19:
        print("Greater than guess no.")
        guess = guess - 1
        print(guess,"attempt are left")
        if guess == 0:
            break
    elif num<19:
        print("Less than guess no.")
        guess = guess - 1
        print(guess, "attempt are left")
        if guess == 0:
            break
    elif num==19:
        print("You have guess correct number",", You have used",guess,"attempt")
        break