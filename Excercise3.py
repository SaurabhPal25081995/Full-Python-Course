# check the numeric from list and print greater than 6

lst = [1,"Saurabh",53,"Pal",False,"dsadas","das","dasd",True,None,"ccc",6,7,4]

for item in lst:
    if str(item).isnumeric() and item>6:
        print(item)
