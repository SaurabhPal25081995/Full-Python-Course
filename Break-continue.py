# i=0
# while(True):
#     if i+1 < 5:
#         i= i+1
#         continue
#     print(i+1, end=" ")
#     if(i==44):
#         break

# Practice, You prgram till continously take ip till your no less than 100
while(True):
    print("Enter the no.")
    num = int(input())
    if num > 100:
        break
    else:
        print("Your no is less than 100 to exit input number greater than 100")
        continue

