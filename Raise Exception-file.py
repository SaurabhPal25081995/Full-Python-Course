name = input("Enter your name")
b = int(input("Enter your salary"))
if b ==0:
    raise ZeroDivisionError("b can not be 0")
if name.isnumeric():
    raise Exception("Number can not be used in name")

print(f"Hi {name}")
