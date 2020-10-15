# abt = {
#     "name" : "Saurabh",
#      "age": 25,
#      "dom": "august",
#      "game" : {"football": {"team1":"p1","team2":"p2"}, "chess":"hobby", "cricket":"timepass"}
# }
# abt['game']['football']['team2']="p3"
# print(abt['game']['football']['team2'])
# print(abt)
#

data = { 
    "football": "best game",
    "cricket" : "popular sports",
    "kabadi" : "traditional sports",
    "hockey" : "national sports"
}
print("Enter your key")
num = input()
print(data[num])

for i in data:
    print(i)


----------------------

#To access both value in list
list1 = [["Saurabh",2],["Gagan",3],["Suraj",4]]
dict1 = dict(list1)
#print(dict1)

# To acces all values
for i in dict1:
    print(dict1[i])

# To access all values by another method
for i in dict1.values():
    print(i)

# To access all key and values
for i,j in dict1.items():
    print(i,"--",j)
