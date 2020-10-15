friend_count = int(input("Enter the no of friends - "))
full_name = []
for i in range(1,friend_count+1):
    full_name.append(input("Enter your friends name - "))
print(f"Your friends are {full_name}")

first_name = []
last_name = []
for i in full_name:
    name = i.split()
    first_name.append(name[0])
    last_name.append(name[1])
    jumbble = last_name[::-1]
    new_names = zip(first_name,jumbble)
    dict_new_name = dict(new_names)
# print("Your friends funniest name is - ",dict_new_name)

print("Funniest names are - ")
for key, value in dict_new_name.items():
    print(key,value)



