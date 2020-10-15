def func(*many,**kwarg):
    print(many)
    for key,value in kwarg.items():
        print(key,value)

lst = ["Saurabh","Pal","Machine learning"]
func(*lst)
lst1 = {"Gagan":"Pal","Profile":"Machine learning"}
print(func(**lst1))

