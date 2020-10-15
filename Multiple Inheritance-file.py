class Player:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        return f"Name of Player is {self.name}, age is {self.age} and gender is {self.gender}"

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def displayemp(self):
        return f"Name of employee is {self.name}, salary is {self.salary} "

class CoolMan(Player,Employee):
    pass

# pal = CoolMan("Saurabh",32)
# print(pal.display())

kumar = CoolMan("Gagan",3000,"Male")
print(kumar.display())